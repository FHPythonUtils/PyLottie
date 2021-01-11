import pylottie

pylottie.convertLottie2Webp("test/file_437.tgs", "test/file_437.webp")
pylottie.convertLottie2GIF("test/file_437.tgs", "test/file_437.gif")

inFiles = ["test/file_43{}.tgs".format(idx) for idx in range (7,10)]
outFiles = ["test/file_0_43{}.webp".format(idx) for idx in range (7,10)]

pylottie.convertMultLottie2Webp(inFiles, outFiles)
