#!/usr/bin/python

from os import listdir
from os.path import isfile, join

def generateFlastaaArray(str):
	str = str.find('&gt;',0,len(str))
	
	
def processFile(fileName):
        print fileName
	f = open(fileName, 'r')
	str = f.read()
	generateFlastaaArray(str)
	print str

mypath = 'flastaa/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for fileName in onlyfiles: 
	processFile(mypath + fileName)

#str.find(str, beg=0 end=len(string))
#print onlyfiles
