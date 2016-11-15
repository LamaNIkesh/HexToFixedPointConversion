# -*- coding: utf-8 -*-
"""
@author: Nikesh Lama
"""


"""
command to run the code: 

python hexToDec-v2.py hexFile.hex datatype
eg python hexToDec 24sf.hex 6

"""


import sys # library required to read and write the files
import numpy as np
import binascii  # this library converts hex string to raw hex, this helps in keeping the hex file size very concise
import os
import os.path
import base64
import struct
global file1
#unsigned datatypes
eight_bit_ufix = 0
sixteen_bit_ufix = 1
twentyFour_bit_ufix = 2
thirtyTwo_bit_ufix = 3
#signed dataTypes
eight_bit_sfix = 4
sixteen_bit_sfix = 5
twentyFour_bit_sfix = 6
thirtyTwo_bit_sfix = 7
#float data type
#not used but can be used
thirtyTwo_bit_float = 8
#This class takes in rawHex and dataType argv and converts into fixed points repr

class HexToDec:
	def __init__(self, rawHex, dataType):
		self.rawHex = rawHex
		self.dataType = dataType

	#takes the fractional part and convert binary into dec representation
	#eg for .1001 => 1/2 + 0/4 + 0 /8 + 1 /16  = 0.5625
	def fractionalPartCal(self):
		print("fractional val cal")
		size = len(self.fractionalpart)
		print (size)
		print (self.fractionalpart)
		decValue = 0.0 
		#this loop iterates and divides each part by 2^n
		#eg for .1001 => 1/2 + 0/4 + 0 /8 + 1 /16 
		for i in range(size):
			decValue +=(float(self.fractionalpart[i])/2**(i + 1))
		print (decValue)
		return decValue
	
	#This method takes the data type and rawHex file and converts it into
	#its correponding fixed point and returns the value as float
	def HexToFixedpoint(self):
		#print ("hex to fix point conversion")
		#based on the dataType the size for integer and fractional
		#part needs to be known
		#intSizeDecSize method returns a dictionary with size for int and fractional part
		#eg. for 8 bit fixedpoint int size is 4 and fractional size is 4
		Sizes = self.intSizeDecSize()
		print (Sizes)
		#assigning the dict values to the variables
		intsize = int(Sizes['intSize'])
		decsize = int(Sizes['decSize'])
		#print (intsize, decsize)
		#hex as a group of bytes
		# 00 00 00 00
		
		#Algorithm for calculting intsize and fractsize of all data types
		#this section generalises the starting and ending index for all 
		#datatypes based on the size of the int part and dec part.  
		#calculates the part for integer and fraction from the hex characters
		#index         01 23 45 67
		#eg hex num:0x 00 00 00 00
		#the indexing is for the hex numbers and not binary
		intpart = rawHex[8 - int(intsize/2):8 - int(intsize/4)]
		#gives starting and ending index for fractional part
		fractionalpart = rawHex[8 - int(decsize/4):8]
		
		#print("Int part:", intpart)
		#print ("fractional part:", fractionalpart)
		#fractional part is same for both signed and unsigned datatypes
		#making the fractionalpart as class variable so that it can be used in other methods too
		self.fractionalpart = bin(int(fractionalpart, 16))[2:].zfill(decsize)
		#################################################
		#for unsigned datatypes
		if dataType == '0' or dataType == '1' or dataType =='2' or dataType == '3':
			intpart = int(intpart,16)
			fractionalpart = self.fractionalPartCal()
			finalValue = intpart + fractionalpart

		#################################################	
		#for signed dataTypes
		#for signed dataTypes the signed bit is checked for negative number
		if dataType == '4' or dataType == '5' or dataType == '6' or dataType == '7':
			binRep = bin(int(intpart, 16))[2:].zfill(intsize)
			print ("binRep:",binRep)
			print (binRep[0])

			#sign bit check for negative numbers
			if binRep[0] == '1':
				#print ("Negative number")
				#print ("intsize:", intsize)
				#print (-(2**(intsize - 1)))
				#print (int(binRep[1:intsize],2))
				NonSignPart = binRep[1:intsize]
				intpart = (-(2**(intsize-1)) + int(NonSignPart,2))
				#print ("intpart:", intpart)
			#getting the fractional part, samme as before
			fractionalpart = self.fractionalPartCal()
			#negative sign is introduced because we dont want to subtract but add
			#however the -ve sign needs to be retained
			#eg we want intpart: -7 and fractionalpart: 0.75 to be -7.75
			#if we just add then we get -6.25
			finalValue = -(-(intpart) + fractionalpart)
		#print ("FinalValue:",finalValue)
		return finalValue
		############################################################
	'''		
	def HexToFloating(self):
		print("Hex to floating point conversion")
		print (struct.unpack('!f', bytes.fromhex(rawHex))[0])
	'''
	#this class method returns a dict of integer size and decimal size based 
	#on the data type
	def intSizeDecSize(self):
		if dataType == '0' or dataType == '4':
			intSize = '4' 
			decSize = '4'
		if dataType == '1' or dataType == '5':
			intSize = '8' 
			decSize = '8'
		if dataType == '2' or dataType == '6':
			intSize = '12' 
			decSize = '12'
		if dataType == '3' or dataType == '7':
			intSize = '16' 
			decSize = '16' 
		#putting the results into dictionary
		return {'intSize':intSize, 'decSize':decSize}

#--------end of class-------------------#
######################################################################################
if __name__ == '__main__':
	#opening the hex file
	file1 = open(sys.argv[1], "rb")
	#reading the block Sizes
	blockSize = 4500
	#read from that block from the file and concatenate the values into string
	with file1:
		block = file1.read(blockSize)
		rawHex = ""
		for ch in block:
			#[2:]helps get rid of 0x and zfill(2) makes sure that the hex
			#are represented into two hex humbers
			rawHex +=hex(ch)[2:].zfill(2)
	#the datatype is typed in as second argv
	dataType = (sys.argv[2])
	#create an obj of class HexToDec with rawHex and dataType argvs
	conversion = HexToDec(rawHex,dataType)
	#conversion.HexToFixpoint()
	#convert the hex numbers with HexToFixedpoint class method
	decimalRepresentaiton = conversion.HexToFixedpoint()
	print ("FinalConversion:", decimalRepresentaiton)

