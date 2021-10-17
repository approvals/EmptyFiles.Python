# EmptyFiles.Python

**TL;DR** Null Object pattern for files. 

<!-- toc -->
<!-- endToc -->

This project will create an empty file of a type requested. 
If possible, that file will be the smallest valid file for that type. For example, an empty jpg will be a 1x1 pixel jpg.

## Usage
This code:

snippet: create_empty_jpg

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