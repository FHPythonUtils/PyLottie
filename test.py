"""Test convert multiple tgs files to webp and gif"""

import time

import pylottie

start = time.time()
pylottie.convertLottie2Webp("test/file_437.tgs", "test/file_437.webp")
pylottie.convertLottie2GIF("test/file_437.tgs", "test/file_437.gif")

inFiles = [f"test/file_43{idx}.tgs" for idx in range(7, 10)]
outFiles = [f"test/file_0_43{idx}" for idx in range(7, 10)]

pylottie.convertMultLottie2ALL(inFiles, outFiles)
end = time.time()

print(f"Time taken - {end - start:.3f}s")
