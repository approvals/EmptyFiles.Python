# EmptyFiles.Python

[![PyPI version](https://img.shields.io/pypi/v/empty-files.svg)](https://pypi.org/project/empty-files)
[![Test](https://github.com/approvals/EmptyFiles.Python/actions/workflows/test.yml/badge.svg)](https://github.com/approvals/EmptyFiles.Python/actions/workflows/test.yml)

**TL;DR** Null Object pattern for files. 

<!-- toc -->
## Contents

  * [Setup](#setup)
  * [Usage](#usage)
  * [Null Object Pattern](#null-object-pattern)
  * [Attributions](#attributions)<!-- endToc -->

This project will create an empty file of a type requested. 
If possible, that file will be the smallest valid file for that type. For example, an empty jpg will be a 1x1 pixel jpg.

## Setup

From [pypi](https://pypi.org/project/empty-files/):

	pip install empty-files


## Usage
This code:

<!-- snippet: create_empty_jpg -->
<a id='snippet-create_empty_jpg'></a>
```py
from empty_files.empty_files import create_empty_file
create_empty_file("temp/empty.jpg")
```
<sup><a href='/tests/test_empty_files.py#L23-L26' title='Snippet source file'>snippet source</a> | <a href='#snippet-create_empty_jpg' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

will create the following [image](tests/test_empty_files.test_sample.approved.jpg)

## Null Object Pattern
**Issue:** null/None causes extra checks in order to avoid errors.

**Solution:** return an empty version of the object, so methods can be used normally.

**Example:** 
if `last_name` returns `""` instead of `None`,  
we can write:

```python
name_length = len(person.last_name())
```

instead of :

```python 
name_length = 0
if (person.last_name())
 name_length = len(person.last_name()) 
```

## Attributions
The empty files are taken from [Simon Cropp's Empty Files](https://github.com/VerifyTests/EmptyFiles/tree/main/index).
