# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 22:40:09 2019

@author: shriya
"""

import pytesseract
from PIL import Image

value=Image.open("download.png")
text = pytesseract.image_to_string(value, config='')    
print("text present in images:",text),