#!/usr/local/bin/python3
# coding: utf-8

"""
Title: upscale_img.py
Author(s): Jonathan A. Gibson
Objectives:
  1. Open the original/input image file.
Notes:
  > Using the "Image" library instead of the "Pillow"/"PIL" library.
"""

import Image
import sys
import os.path

if(len(sys.argv) != 2):
  print("ERROR::160::BAD_ARGUMENTS")
  print("Run program with the following format: \'python3 upscale_img.py \"<img_file>.jpg\"\'; alternatively use \'make run\' to run with default Makefile settings.\n")
  sys.exit()

im = Image.open(sys.argv[1])   
out = Image.new('I', im.size, 0xffffff)

width, height = im.size
for x in range(width):
    for y in range(heigh
        r,g,b = im.getpixel((x,y))
        if b < g and b < r or r==g==b:
            out.putpixel((x,y), 0)

out.save('bar.png')