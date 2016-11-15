# HexToFixedPointConversion

Simple scripts that takes in raw hex of 32 bits and converts to required fixed point repr

#######################################
command to run the code: 

locate the directory with the code and hex file. then type in the commands below

python hexToDec.py hexFile.hex datatype(refer to fixed point data types indicated with a number)
eg python hexToDec 24sf.hex 6
########################################

######Fixed poin data types#############

#unsigned datatypes (uf)
eight_bit_ufix = 0 
sixteen_bit_ufix = 1
twentyFour_bit_ufix = 2
thirtyTwo_bit_ufix = 3

#signed dataTypes  (sf)
eight_bit_sfix = 4
sixteen_bit_sfix = 5
twentyFour_bit_sfix = 6
thirtyTwo_bit_sfix = 7

##########################################

all hex files are 32 bits long.
XX-XX-XX-XX
If 8 bit fixed point is converted, the 8 bits from the LSB are taken into account and rest are discarded. 
