"""test convert multiple tgs files to webp and gif"""

from __future__ import annotations

import sys
import time
from pathlib import Path

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))

import pylottie

start = time.time()
pylottie.convertLottie2Webp(f"{THISDIR}/data/file_437.tgs", f"{THISDIR}/data/file_437.webp")
pylottie.convertLottie2GIF(f"{THISDIR}/data/file_437.tgs", f"{THISDIR}/data/file_437.gif")

inFiles = [f"{THISDIR}/data/file_43{idx}.tgs" for idx in range(7, 10)]
outFiles = [f"{THISDIR}/data/file_0_43{idx}" for idx in range(7, 10)]

pylottie.convertMultLottie2ALL(inFiles, outFiles)
end = time.time()

print(f"Time taken - {end - start:.3f}s")
