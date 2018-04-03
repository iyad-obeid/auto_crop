#!/usr/bin/env python

import sys
import numpy as np
from scipy import misc

def main(argv):
	if len(sys.argv)==1:
		print("please supply a filename")
		sys.exit

	for fname in sys.argv[1:]:
		try:
			img = misc.imread(fname)
			img = shaveLeft(img)
			img = shaveRight(img)
			img = shaveTop(img)
			img = shaveBottom(img)
			misc.imsave(fname,img)
			print("complete: " , fname)
		except:
			print("file not found")


def shaveLeft(img):
# shave off the left
	i = 0
	kg = 1
	while kg:
		if((img[:,i,0]==255).all()):
			i = i + 1
		else:
			kg = 0
		if (i==img.shape[1]):
			kg = 0
	img = img[:,i:,:]
	return img

def shaveRight(img):
# shave off the right
	i = img.shape[1]-1
	kg = 1
	while kg:
		if((img[:,i,0]==255).all()):
			i = i - 1
		else:
			kg = 0
		if (i==0):
			kg = 0
	i = i + 1
	img = img[:,0:i,:]
	return img

def shaveTop(img):
# shave off the top
	i = 0
	kg = 1
	while kg:
		if((img[i,:,0]==255).all()):
			i = i + 1
		else:
			kg = 0
		if (i==img.shape[0]):
			kg = 0
	img = img[i:,:,:]
	return img

def shaveBottom(img):
# shave off the bottom
	i = img.shape[0]-1
	kg = 1
	while kg:
		if((img[i,:,0]==255).all()):
			i = i - 1
		else:
			kg = 0
		if (i==0):
			kg = 0
	i = i + 1
	img = img[0:i,:,:]
	return(img)




if __name__ == "__main__":
	main(sys.argv)
