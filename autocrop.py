#!/usr/bin/env python

import sys
import numpy as np
from scipy import misc

fname = ""
if len(sys.argv)==2:
	fname = sys.argv[1]
else:
	print("please supply a filename")
	sys.exit

img = misc.imread(fname)

# shave off the left
i = 0
kg = 1
while kg:
	if((img[:,i,0]==255).all()):
		i = i + 1
	else:
		kg = 0
	if (i==img.shape[0]):
		kg = 0
img = img[:,i:,:]

# shave off the right
i = img.shape[1]-1
kg = 1
while kg:
	if((img[:,i,0]==255).all()):
		i = i - 1
	else:
		kg = 0
	if (i==img.shape[0]):
		kg = 0
i = i + 1
img = img[:,0:i,:]

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

# shave off the bottom
i = img.shape[0]-1
kg = 1
while kg:
	if((img[i,:,0]==255).all()):
		i = i - 1
	else:
		kg = 0
	if (i==img.shape[0]):
		kg = 0
i = i + 1
img = img[0:i,:,:]



misc.imsave(fname,img)
