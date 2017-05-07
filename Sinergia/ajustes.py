import os

dirbase = os.path.dirname(os.path.realpath(__file__))

dirmg = os.path.join(dirbase, 'img')

def mg(img):
	return os.path.join(dirmg, img)