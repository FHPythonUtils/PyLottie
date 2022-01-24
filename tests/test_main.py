import sys
from pathlib import Path

from imgcompare import imgcompare
from PIL import Image

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))

import pylottie


def test_convertLottie2Webp():
	"""test_convertLottie2Webp"""
	pylottie.convertLottie2Webp(f"{THISDIR}/data/file_437.tgs", f"{THISDIR}/data/file_437.webp")
	output = Image.open(f"{THISDIR}/data/file_437.webp")
	expected = Image.open(f"{THISDIR}/data/file_0_437_expected.webp")
	assert output.n_frames == expected.n_frames
	for frame in range(output.n_frames):
		output.seek(frame)
		expected.seek(frame)
		assert imgcompare.is_equal(
			output,
			expected,
			tolerance=0.2,
		)


def test_convertLottie2GIF():
	"""test_convertLottie2GIF"""
	pylottie.convertLottie2GIF(f"{THISDIR}/data/file_437.tgs", f"{THISDIR}/data/file_437.gif")
	output = Image.open(f"{THISDIR}/data/file_437.gif")
	expected = Image.open(f"{THISDIR}/data/file_0_437_expected.gif")
	assert output.n_frames == expected.n_frames
	for frame in range(output.n_frames):
		output.seek(frame)
		expected.seek(frame)
		assert imgcompare.is_equal(
			output,
			expected,
			tolerance=0.2,
		)


def test_convertMultLottie2Webp():
	"""test_convertMultLottie2Webp"""
	inFiles = [f"{THISDIR}/data/file_43{idx}.tgs" for idx in range(7, 10)]
	outFiles = [f"{THISDIR}/data/file_0_43{idx}.webp" for idx in range(7, 10)]
	pylottie.convertMultLottie2Webp(inFiles, outFiles)
	for file in outFiles:
		assert Path(f"{file}").exists()
		assert (
			Image.open(file).n_frames
			== Image.open(file.replace(".webp", "_expected.webp")).n_frames
		)


if __name__ == "__main__":
	test_convertLottie2Webp()
	test_convertLottie2GIF()
	test_convertMultLottie2Webp()
