#!/bin/python3

print('Input int: ')
myInput = input()
myString = []

for i in myInput:
	myString.append(i)

for i in range(len(myString)-1, -1, -1):

	if (i != len(myString)-1) and (carry == 0):
		break
	carry = 0	
	if myString[i] == '0':
		myString[i] = '1'
	elif myString[i] == '1':
		myString[i] = '2'
	elif myString[i] == '2':
		myString[i] = '3'
	elif myString[i] == '3':
		myString[i] = '4'
	elif myString[i] == '4':
		myString[i] = '5'
	elif myString[i] == '5':
		myString[i] = '6'
	elif myString[i] == '6':
		myString[i] = '7'
	elif myString[i] == '7':
		myString[i] = '8'
	elif myString[i] == '8':
		myString[i] = '9'
	elif myString[i] == '9':
		myString[i] = '0'
		if (i == 0):
			myString[i] = '10'
		carry = 1

	else:
		print('Please input an integer.')			
	
print(''.join(myString))	
