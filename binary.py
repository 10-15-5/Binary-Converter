import re

def validate(binary, validated):
	
	if re.search('[^01]', binary): 
		print('Your binary value must only contain 1s and 0s!')
	elif (len(binary) % 8) != 0:
		print('Not in Bytes man')
	else:
		validated = True
	
	return binary, validated


def bitstobytes(binary):
	length = 8
	newbinary = ' '.join(binary[i:i+length] for i in range(0, len(binary), length))
	
	displaystring(newbinary)

def displaystring(binary):
	binaryvalues = binary.split()

	asciistring = ''

	for binaryvalue in binaryvalues:
		integer = int(binaryvalue, 2)
		
		asciichar = chr(integer)
		
		asciistring += asciichar
	
	print('It says: ', asciistring)


print('WELCOME TO THE BINARY - STRING DISPLAY')

validated = False
while validated == False:
	binarystring = input('Please enter your binary string for translation: ')
	binarystring = binarystring.replace(' ','')
	binary, validated = validate(binarystring, validated)
	
bitstobytes(binary)
