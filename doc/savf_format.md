# Simple ASCII Video Format (SAVF)

## Introduction

SAVF is designed to store ASCII video stream using Huffman code. The stream must be generated by the `Ascgen2` utility.



## Specification

**Header**: SAVF has a 32-bit header that indicates the total frame length and the number of mapping entries following.

```
31 (MSB)         24 23                                      (LSB) 0
|----------------------------------------------------------------|
|  #mapping_entry  |                   #frames                   |
|----------------------------------------------------------------|
```



**Character Mapping Table**:

Here we use the fact that only a subset of ASCII 

```
31 (MSB)   24 23                                           (LSB) 0
|----------------------------------------------------------------|
|   origin   |   total bit count |           mapping             |
|----------------------------------------------------------------|
```


