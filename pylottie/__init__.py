from __future__ import annotations
"""Support for animated stickers
"""
import os
import gzip
import json
import asyncio
from pathlib import Path
from shutil import rmtree
from pyppeteer import launch
from PIL import Image
THISDIR = str(Path(__file__).resolve().parent)



def convertLottie2GIF(fileName: str, newFileName: str, quality: int=0):
	"""Convert to webp

	Args:
		fileName (str): file path of the lottie file
		newFileName (str): name of the file to write
		quality (int, optional): Quality of the returned sequence. Defaults to 0.
	"""
	convertMultLottie2GIF([fileName], [newFileName], quality)
	rmtree("temp", ignore_errors=True)

def convertLottie2Webp(fileName: str, newFileName: str, quality: int=0):
	"""Convert to webp

	Args:
		fileName (str): file path of the lottie file
		newFileName (str): name of the file to write
		quality (int, optional): Quality of the returned sequence. Defaults to 0.
	"""
	convertMultLottie2Webp([fileName], [newFileName], quality)
	rmtree("temp", ignore_errors=True)

def convertMultLottie2GIF(fileNames: list[str], newFileNames: list[str], quality: int=0):
	"""Convert to gif

	Args:
		fileNames (list[str]): list of file path to the lottie files
		newFileNames (list[str]): name of the files to write
		quality (int, optional): Quality of the returned sequence. Defaults to 0.
	"""
	imageDataList = convertLotties2PIL(fileNames, quality)
	for index, imageData in enumerate(imageDataList):
		images = imageData[0]
		duration = imageData[1]
		images[0].save(newFileNames[index], save_all=True, append_images=images[1:],
		duration=duration*1000/len(images), loop=0, transparency=0, disposal=2)
	rmtree("temp", ignore_errors=True)

def convertMultLottie2Webp(fileNames: list[str], newFileNames: list[str], quality: int=0):
	"""Convert to webp

	Args:
		fileNames (list[str]): list of file path to the lottie files
		newFileNames (list[str]): name of the files to write
		quality (int, optional): Quality of the returned sequence. Defaults to 0.
	"""
	imageDataList = convertLotties2PIL(fileNames, quality)
	for index, imageData in enumerate(imageDataList):
		images = imageData[0]
		duration = imageData[1]
		images[0].save(newFileNames[index], save_all=True, append_images=images[1:],
		duration=int(duration*1000/len(images)), loop=0)
	rmtree("temp", ignore_errors=True)



def resQuality(quality):
	qualityMap = [3,2,1]
	if quality >= len(qualityMap) or quality < 0:
		return 2
	return qualityMap[quality]


def convertLotties2PIL(fileNames: list[str], quality: int=0) -> list[tuple[list[Image.Image], float]]:
	"""Convert list of lottie files to a list of images with a duration

	Args:
		fileNames (list[str]): list of file paths of the lottie files
		quality (int, optional): Quality of the returned sequence. Defaults to 0.

	Returns:
		list[tuple[list[Image.Image], float]]: pil images to write to gif/ webp and duration
	"""
	lotties = []
	for fileName in fileNames:
		with open(fileName, "rb") as binfile:
			mn = binfile.read(2)
			binfile.seek(0)
			if mn == b'\x1f\x8b': # gzip magic number
				archive = gzip.open(fileName, "rb")
				lottie = json.load(archive)
			else:
				lottie = json.load(open(fileName))
		lotties.append(lottie)
	step = resQuality(quality)
	frameData = asyncio.get_event_loop(
	).run_until_complete(recordLotties([json.dumps(lottie) for lottie in lotties], step))
	imageDataList = []
	for index, frameDataInstance in enumerate(frameData):
		images = []
		duration = frameDataInstance[0]
		numFrames = frameDataInstance[1]
		for frame in range(0, numFrames, step):
			images.append(Image.open("temp/temp{}_{}.png".format(index, frame)))
		imageDataList.append([images, duration])
	return imageDataList


async def recordLotties(lottieData: list[str], step: int) -> list[tuple[int, int]]:
	"""Record the lottie data to a set of images

	Args:
		lottieData (str): lottie data as string
		step (int): Step by, Related to quality of the returned sequence.

	Returns:
		tuple[int, int]: duration and number of frames
	"""
	# Make temp dir
	if os.path.isdir("temp"):
		pass
	else:
		os.mkdir("temp")
	# Create pyppeteer instance
	browser = await launch(headless=True,
	options={'args': ['--no-sandbox', "--disable-web-security",
	"--allow-file-access-from-files"]}) # yapf: disable
	# Convert lottie to png files and generate 'frameData'
	frameData = []
	for index, lottieDataInstance in enumerate(lottieData):
		page = await browser.newPage()
		lottie = json.loads(lottieDataInstance)
		html = open(THISDIR + "/lottie.html").read().replace("lottieData",
		lottieDataInstance).replace("WIDTH", str(lottie["w"])).replace("HEIGHT", str(lottie["h"]))
		await page.setContent(html)
		await page.waitForSelector('.ready')
		duration = await page.evaluate("() => duration")
		numFrames = await page.evaluate("() => numFrames")
		pageFrame = page.mainFrame
		rootHandle = await pageFrame.querySelector('#root')
		# Take a screenshot of each frame
		for frame in range(0, numFrames, step):
			await rootHandle.screenshot({
			'path': 'temp/temp{}_{}.png'.format(index, frame), "omitBackground": True})
			await page.evaluate("animation.goToAndStop({}, true)".format(frame + 1))
		frameData.append([duration, numFrames])
		await page.close()
	return frameData
