import time
import pylottie

start = time.time()
pylottie.convertLottie2Webp("test/file_437.tgs", "test/file_437.webp")
pylottie.convertLottie2GIF("test/file_437.tgs", "test/file_437.gif")

inFiles = ["test/file_43{}.tgs".format(idx) for idx in range (7,10)]
outFiles = ["test/file_0_43{}".format(idx) for idx in range (7,10)]

pylottie.convertMultLottie2ALL(inFiles, outFiles)
end = time.time()

print('Time taken - {:.3f}s'.format(end - start))
