# pylottie

> Auto-generated documentation for [pylottie](../../pylottie/__init__.py) module.

- [Pylottie](../README.md#pylottie-index) / [Modules](../README.md#pylottie-modules) / pylottie
    - [convertLottie2ALL](#convertlottie2all)
    - [convertLottie2GIF](#convertlottie2gif)
    - [convertLottie2Webp](#convertlottie2webp)
    - [convertLotties2PIL](#convertlotties2pil)
    - [convertMultLottie2ALL](#convertmultlottie2all)
    - [convertMultLottie2GIF](#convertmultlottie2gif)
    - [convertMultLottie2Webp](#convertmultlottie2webp)
    - [recordLotties](#recordlotties)
    - [recordSingleLottie](#recordsinglelottie)
    - [resQuality](#resquality)

## convertLottie2ALL

[[find in source code]](../../pylottie/__init__.py#L15)

```python
def convertLottie2ALL(fileName: str, newFileName: str, quality: int = 1):
```

Convert to gif and webp

#### Arguments

- `fileName` *str* - file path of the lottie file
- `newFileName` *str* - name of the file to write (omit file ext)
- `quality` *int, optional* - Quality of the returned sequence. Defaults to 1.

## convertLottie2GIF

[[find in source code]](../../pylottie/__init__.py#L25)

```python
def convertLottie2GIF(fileName: str, newFileName: str, quality: int = 1):
```

Convert to webp

#### Arguments

- `fileName` *str* - file path of the lottie file
- `newFileName` *str* - name of the file to write
- `quality` *int, optional* - Quality of the returned sequence. Defaults to 1.

## convertLottie2Webp

[[find in source code]](../../pylottie/__init__.py#L35)

```python
def convertLottie2Webp(fileName: str, newFileName: str, quality: int = 1):
```

Convert to webp

#### Arguments

- `fileName` *str* - file path of the lottie file
- `newFileName` *str* - name of the file to write
- `quality` *int, optional* - Quality of the returned sequence. Defaults to 1.

## convertLotties2PIL

[[find in source code]](../../pylottie/__init__.py#L104)

```python
def convertLotties2PIL(
    fileNames: list[str],
    quality: int = 1,
) -> list[tuple[(list[Image.Image], float)]]:
```

Convert list of lottie files to a list of images with a duration

#### Arguments

- `fileNames` *list[str]* - list of file paths of the lottie files
- `quality` *int, optional* - Quality of the returned sequence. Defaults to 1.

#### Returns

- `list[tuple[list[Image.Image],` *float]]* - pil images to write to gif/ webp and duration

## convertMultLottie2ALL

[[find in source code]](../../pylottie/__init__.py#L45)

```python
def convertMultLottie2ALL(
    fileNames: list[str],
    newFileNames: list[str],
    quality: int = 1,
):
```

Convert to gif and webp

#### Arguments

- `fileNames` *list[str]* - list of file path to the lottie files
- `newFileNames` *list[str]* - name of the files to write (omit file ext)
- `quality` *int, optional* - Quality of the returned sequence. Defaults to 1.

## convertMultLottie2GIF

[[find in source code]](../../pylottie/__init__.py#L63)

```python
def convertMultLottie2GIF(
    fileNames: list[str],
    newFileNames: list[str],
    quality: int = 1,
):
```

Convert to gif

#### Arguments

- `fileNames` *list[str]* - list of file path to the lottie files
- `newFileNames` *list[str]* - name of the files to write
- `quality` *int, optional* - Quality of the returned sequence. Defaults to 1.

## convertMultLottie2Webp

[[find in source code]](../../pylottie/__init__.py#L79)

```python
def convertMultLottie2Webp(
    fileNames: list[str],
    newFileNames: list[str],
    quality: int = 1,
):
```

Convert to webp

#### Arguments

- `fileNames` *list[str]* - list of file path to the lottie files
- `newFileNames` *list[str]* - name of the files to write
- `quality` *int, optional* - Quality of the returned sequence. Defaults to 1.

## recordLotties

[[find in source code]](../../pylottie/__init__.py#L139)

```python
async def recordLotties(
    lottieData: list[str],
    quality: int,
) -> list[tuple[(int, int)]]:
```

Record the lottie data to a set of images

#### Arguments

- `lottieData` *str* - lottie data as string
- `quality` *int, optional* - Quality of the returned sequence.

#### Returns

- `tuple[int,` *int]* - duration and number of frames

## recordSingleLottie

[[find in source code]](../../pylottie/__init__.py#L168)

```python
async def recordSingleLottie(browser, lottieDataInstance, quality, index):
```

## resQuality

[[find in source code]](../../pylottie/__init__.py#L97)

```python
def resQuality(quality: int, numFrames: int, duration: int):
```
