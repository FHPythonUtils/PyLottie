# pylottie

> Auto-generated documentation for [pylottie](../../pylottie/__init__.py) module.

- [Pylottie](../README.md#pylottie-index) / [Modules](../README.md#pylottie-modules) / pylottie
    - [convertLottie2GIF](#convertlottie2gif)
    - [convertLottie2Webp](#convertlottie2webp)
    - [convertLotties2PIL](#convertlotties2pil)
    - [convertMultLottie2GIF](#convertmultlottie2gif)
    - [convertMultLottie2Webp](#convertmultlottie2webp)
    - [recordLotties](#recordlotties)
    - [resQuality](#resquality)

## convertLottie2GIF

[[find in source code]](../../pylottie/__init__.py#L16)

```python
def convertLottie2GIF(fileName: str, newFileName: str, quality: int = 0):
```

Convert to webp

#### Arguments

- `fileName` *str* - file path of the lottie file
- `newFileName` *str* - name of the file to write
- `quality` *int, optional* - Quality of the returned sequence. Defaults to 0.

## convertLottie2Webp

[[find in source code]](../../pylottie/__init__.py#L27)

```python
def convertLottie2Webp(fileName: str, newFileName: str, quality: int = 0):
```

Convert to webp

#### Arguments

- `fileName` *str* - file path of the lottie file
- `newFileName` *str* - name of the file to write
- `quality` *int, optional* - Quality of the returned sequence. Defaults to 0.

## convertLotties2PIL

[[find in source code]](../../pylottie/__init__.py#L79)

```python
def convertLotties2PIL(
    fileNames: list[str],
    quality: int = 0,
) -> list[tuple[(list[Image.Image], float)]]:
```

Convert list of lottie files to a list of images with a duration

#### Arguments

- `fileNames` *list[str]* - list of file paths of the lottie files
- `quality` *int, optional* - Quality of the returned sequence. Defaults to 0.

#### Returns

- `list[tuple[list[Image.Image],` *float]]* - pil images to write to gif/ webp and duration

## convertMultLottie2GIF

[[find in source code]](../../pylottie/__init__.py#L38)

```python
def convertMultLottie2GIF(
    fileNames: list[str],
    newFileNames: list[str],
    quality: int = 0,
):
```

Convert to gif

#### Arguments

- `fileNames` *list[str]* - list of file path to the lottie files
- `newFileNames` *list[str]* - name of the files to write
- `quality` *int, optional* - Quality of the returned sequence. Defaults to 0.

## convertMultLottie2Webp

[[find in source code]](../../pylottie/__init__.py#L54)

```python
def convertMultLottie2Webp(
    fileNames: list[str],
    newFileNames: list[str],
    quality: int = 0,
):
```

Convert to webp

#### Arguments

- `fileNames` *list[str]* - list of file path to the lottie files
- `newFileNames` *list[str]* - name of the files to write
- `quality` *int, optional* - Quality of the returned sequence. Defaults to 0.

## recordLotties

[[find in source code]](../../pylottie/__init__.py#L114)

```python
async def recordLotties(
    lottieData: list[str],
    step: int,
) -> list[tuple[(int, int)]]:
```

Record the lottie data to a set of images

#### Arguments

- `lottieData` *str* - lottie data as string
- `step` *int* - Step by, Related to quality of the returned sequence.

#### Returns

- `tuple[int,` *int]* - duration and number of frames

## resQuality

[[find in source code]](../../pylottie/__init__.py#L72)

```python
def resQuality(quality):
```
