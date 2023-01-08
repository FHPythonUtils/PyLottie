# Pylottie

[Pylottie Index](../README.md#pylottie-index) /
Pylottie

> Auto-generated documentation for [pylottie](../../../pylottie/__init__.py) module.

- [Pylottie](#pylottie)
  - [convertLottie2ALL](#convertlottie2all)
  - [convertLottie2GIF](#convertlottie2gif)
  - [convertLottie2Webp](#convertlottie2webp)
  - [convertLotties2PIL](#convertlotties2pil)
  - [convertMultLottie2ALL](#convertmultlottie2all)
  - [convertMultLottie2GIF](#convertmultlottie2gif)
  - [convertMultLottie2Webp](#convertmultlottie2webp)
  - [recordLotties](#recordlotties)
  - [recordSingleLottie](#recordsinglelottie)

## convertLottie2ALL

[Show source in __init__.py:19](../../../pylottie/__init__.py#L19)

Convert to gif and webp

#### Arguments

- `fileName` *str* - file path of the lottie file
- `newFileName` *str* - name of the file to write (omit file ext)
- `quality` *int, optional* - Quality of the returned sequence. Defaults to 1.

#### Signature

```python
def convertLottie2ALL(fileName: str, newFileName: str, quality: int = 1):
    ...
```



## convertLottie2GIF

[Show source in __init__.py:30](../../../pylottie/__init__.py#L30)

Convert to gif

#### Arguments

- `fileName` *str* - file path of the lottie file
- `newFileName` *str* - name of the file to write
- `quality` *int, optional* - Quality of the returned sequence. Defaults to 1.

#### Signature

```python
def convertLottie2GIF(fileName: str, newFileName: str, quality: int = 1):
    ...
```



## convertLottie2Webp

[Show source in __init__.py:41](../../../pylottie/__init__.py#L41)

Convert to webp

#### Arguments

- `fileName` *str* - file path of the lottie file
- `newFileName` *str* - name of the file to write
- `quality` *int, optional* - Quality of the returned sequence. Defaults to 1.

#### Signature

```python
def convertLottie2Webp(fileName: str, newFileName: str, quality: int = 1):
    ...
```



## convertLotties2PIL

[Show source in __init__.py:137](../../../pylottie/__init__.py#L137)

Convert list of lottie files to a list of images with a duration.

#### Arguments

- `fileNames` *list[str]* - list of file paths of the lottie files
- `quality` *int, optional* - Quality of the returned sequence. Defaults to 1.

#### Returns

- `list[tuple[list[Image],` *float]]* - pil images to write to gif/ webp and duration

#### Signature

```python
def convertLotties2PIL(
    fileNames: list[str], quality: int = 1
) -> list[tuple[list[Image.Image], float]]:
    ...
```



## convertMultLottie2ALL

[Show source in __init__.py:52](../../../pylottie/__init__.py#L52)

Convert to gif and webp

#### Arguments

- `fileNames` *list[str]* - list of file path to the lottie files
- `newFileNames` *list[str]* - name of the files to write (omit file ext)
- `quality` *int, optional* - Quality of the returned sequence. Defaults to 1.

#### Signature

```python
def convertMultLottie2ALL(
    fileNames: list[str], newFileNames: list[str], quality: int = 1
):
    ...
```



## convertMultLottie2GIF

[Show source in __init__.py:84](../../../pylottie/__init__.py#L84)

Convert to gif

#### Arguments

- `fileNames` *list[str]* - list of file path to the lottie files
- `newFileNames` *list[str]* - name of the files to write
- `quality` *int, optional* - Quality of the returned sequence. Defaults to 1.

#### Signature

```python
def convertMultLottie2GIF(
    fileNames: list[str], newFileNames: list[str], quality: int = 1
):
    ...
```



## convertMultLottie2Webp

[Show source in __init__.py:108](../../../pylottie/__init__.py#L108)

Convert to webp

#### Arguments

- `fileNames` *list[str]* - list of file path to the lottie files
- `newFileNames` *list[str]* - name of the files to write
- `quality` *int, optional* - Quality of the returned sequence. Defaults to 1.

#### Signature

```python
def convertMultLottie2Webp(
    fileNames: list[str], newFileNames: list[str], quality: int = 1
):
    ...
```



## recordLotties

[Show source in __init__.py:177](../../../pylottie/__init__.py#L177)

Record the lottie data to a set of images

#### Arguments

- `lottieData` *str* - lottie data as string
- `quality` *int, optional* - Quality of the returned sequence.

#### Returns

- `list[list[int]]` - duration and number of frames

#### Signature

```python
def recordLotties(lottieData: list[str], quality: int) -> list[list[int]]:
    ...
```



## recordSingleLottie

[Show source in __init__.py:206](../../../pylottie/__init__.py#L206)

#### Signature

```python
def recordSingleLottie(browser, lottieDataInstance, quality, index) -> list[int]:
    ...
```


