"""Support for animated stickers
"""
from __future__ import annotations

import asyncio
import gzip
import json
import os
from math import ceil
from pathlib import Path
from shutil import rmtree

from PIL import Image
from pyppeteer import launch

THISDIR = str(Path(__file__).resolve().parent)


def convertLottie2ALL(fileName: str, newFileName: str, quality: int = 1):
	"""Convert to gif and webp

	Args:
		fileName (str): file path of the lottie file
		newFileName (str): name of the file to write (omit file ext)
		quality (int, optional): Quality of the returned sequence. Defaults to 1.
	"""
	convertMultLottie2ALL([fileName], [newFileName], quality)


def convertLottie2GIF(fileName: str, newFileName: str, quality: int = 1):
	"""Convert to gif

	Args:
		fileName (str): file path of the lottie file
		newFileName (str): name of the file to write
		quality (int, optional): Quality of the returned sequence. Defaults to 1.
	"""
	convertMultLottie2GIF([fileName], [newFileName], quality)


def convertLottie2Webp(fileName: str, newFileName: str, quality: int = 1):
	"""Convert to webp

	Args:
		fileName (str): file path of the lottie file
		newFileName (str): name of the file to write
		quality (int, optional): Quality of the returned sequence. Defaults to 1.
	"""
	convertMultLottie2Webp([fileName], [newFileName], quality)


def convertMultLottie2ALL(fileNames: list[str], newFileNames: list[str], quality: int = 1):
	"""Convert to gif and webp

	Args:
		fileNames (list[str]): list of file path to the lottie files
		newFileNames (list[str]): name of the files to write (omit file ext)
		quality (int, optional): Quality of the returned sequence. Defaults to 1.
	"""
	imageDataList = convertLotties2PIL(fileNames, quality)
	for index, imageData in enumerate(imageDataList):
		images = imageData[0]
		duration = imageData[1]
		images[0].save(
			newFileNames[index] + ".gif",
			append_images=images[1:],
			duration=duration * 1000 / len(images),
			version="GIF89a",
			transparency=0,
			disposal=2,
			save_all=True,
			loop=0,
		)
		images[0].save(
			newFileNames[index] + ".webp",
			save_all=True,
			append_images=images[1:],
			duration=int(duration * 1000 / len(images)),
			loop=0,
		)
	rmtree("temp", ignore_errors=True)


def convertMultLottie2GIF(fileNames: list[str], newFileNames: list[str], quality: int = 1):
	"""Convert to gif

	Args:
		fileNames (list[str]): list of file path to the lottie files
		newFileNames (list[str]): name of the files to write
		quality (int, optional): Quality of the returned sequence. Defaults to 1.
	"""
	imageDataList = convertLotties2PIL(fileNames, quality)
	for index, imageData in enumerate(imageDataList):
		images = imageData[0]
		duration = imageData[1]
		images[0].save(
			newFileNames[index],
			save_all=True,
			append_images=images[1:],
			duration=duration * 1000 / len(images),
			loop=0,
			transparency=0,
			disposal=2,
		)
	rmtree("temp", ignore_errors=True)


def convertMultLottie2Webp(fileNames: list[str], newFileNames: list[str], quality: int = 1):
	"""Convert to webp

	Args:
		fileNames (list[str]): list of file path to the lottie files
		newFileNames (list[str]): name of the files to write
		quality (int, optional): Quality of the returned sequence. Defaults to 1.
	"""
	imageDataList = convertLotties2PIL(fileNames, quality)
	for index, imageData in enumerate(imageDataList):
		images = imageData[0]
		duration = imageData[1]
		images[0].save(
			newFileNames[index],
			save_all=True,
			append_images=images[1:],
			duration=int(duration * 1000 / len(images)),
			loop=0,
		)
	rmtree("temp", ignore_errors=True)


def _resQuality(quality: int, numFrames: int, duration: int):
	qualityMap = [10, 15, 20, 30]
	if quality >= len(qualityMap) or quality < 0:
		return 2
	return ceil((numFrames / duration) / qualityMap[quality])


def convertLotties2PIL(
	fileNames: list[str], quality: int = 1
) -> list[tuple[list[Image.Image], float]]:
	"""Convert list of lottie files to a list of images with a duration.

	Args:
		fileNames (list[str]): list of file paths of the lottie files
		quality (int, optional): Quality of the returned sequence. Defaults to 1.

	Returns:
		list[tuple[list[Image], float]]: pil images to write to gif/ webp and duration
	"""
	lotties = []
	for fileName in fileNames:
		with open(fileName, "rb") as binfile:
			magicNumber = binfile.read(2)
			binfile.seek(0)
			if magicNumber == b"\x1f\x8b":  # gzip magic number
				try:
					archive = gzip.open(fileName, "rb")
					lottie = json.load(archive)
				except gzip.BadGzipFile:
					continue
			else:
				lottie = json.loads(Path(fileName).read_text(encoding="utf-8"))
		lotties.append(lottie)
	frameData = asyncio.get_event_loop().run_until_complete(
		recordLotties([json.dumps(lottie) for lottie in lotties], quality)
	)
	imageDataList = []
	for index, frameDataInstance in enumerate(frameData):
		images = []
		duration = frameDataInstance[0]
		numFrames = frameDataInstance[1]
		step = frameDataInstance[2]
		for frame in range(0, numFrames, step):
			images.append(Image.open(f"temp/temp{index}_{frame}.png"))
		imageDataList.append([images, duration])
	return imageDataList


async def recordLotties(lottieData: list[str], quality: int) -> list[list[int]]:
	"""Record the lottie data to a set of images

	Args:
		lottieData (str): lottie data as string
		quality (int, optional): Quality of the returned sequence.

	Returns:
		list[list[int]]: duration and number of frames
	"""
	# Make temp dir
	if os.path.isdir("temp"):
		pass
	else:
		os.mkdir("temp")
	# Create pyppeteer instance
	browser = await launch(
		headless=True,
		options={
			"args": ["--no-sandbox", "--disable-web-security", "--allow-file-access-from-files"]
		},
	)
	# Convert lottie to png files and generate 'frameData'
	tasks = []
	for index, lottieDataInstance in enumerate(lottieData):
		task = asyncio.ensure_future(
			recordSingleLottie(browser, lottieDataInstance, quality, index)
		)
		tasks.append(task)
	frameData = await asyncio.gather(*tasks)
	await browser.close()
	return frameData  # type:ignore


async def recordSingleLottie(browser, lottieDataInstance, quality, index) -> list[int]:
	page = await browser.newPage()
	lottie = json.loads(lottieDataInstance)
	html = (
		Path(THISDIR + "/lottie.html")
		.read_text(encoding="utf-8")
		.replace("lottieData", lottieDataInstance)
		.replace("WIDTH", str(lottie["w"]))
		.replace("HEIGHT", str(lottie["h"]))
	)
	await page.setContent(html)
	await page.waitForSelector(".ready")
	duration = await page.evaluate("() => duration")
	numFrames = await page.evaluate("() => numFrames")
	pageFrame = page.mainFrame
	rootHandle = await pageFrame.querySelector("#root")
	# Take a screenshot of each frame
	step = _resQuality(quality, numFrames, duration)
	for frame in range(0, numFrames, step):
		await rootHandle.screenshot(
			{"path": f"temp/temp{index}_{frame}.png", "omitBackground": True}
		)
		await page.evaluate(f"animation.goToAndStop({frame + 1}, true)")
	await page.close()
	return [duration, numFrames, step]
