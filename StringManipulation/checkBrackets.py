#!/bin/python3

def getMatched(myList):
	openList = ['(', '{', '[', '<']
	closeList = [')', '}', ']', '>']
	resultList = []

	for i in range(len(myList)):

		# Last element in myList
		if i == len(myList)-1 and len(resultList) != 0:
			# print('No more item')
			return False
			
		
		# If input is close, check if the close matches last element in the list
		if myList[i] in closeList:

			if len(resultList) == 0:
				# print('No item in resultList')
				return False
			if myList[i] == closeList[0] and resultList[-1] != openList[0]:
				return False
			if myList[i] == closeList[1] and resultList[-1] != openList[1]:
				return False
			if myList[i] == closeList[2] and resultList[-1] != openList[2]:
				return False
			if myList[i] == closeList[3] and resultList[-1] != openList[3]:
				return False
			resultList.pop(-1)

		# If input is open, add it to the list 
		if myList[i] in openList:
			resultList.append(myList[i])
			
	return True


if __name__ == '__main__':

	getInput = 'abc.di{[]}{}{}()[] expected: True' #input()
	print(getInput)
	result = getMatched(getInput)
	print(result)
	print('------------')

	getInput = 'abc.di{[]}{}{}()[]{[({})]} expected: True'
	print(getInput)
	result = getMatched(getInput)
	print(result)
	print('------------')

	getInput = 'abc.di{[]}{@}([] expected: False'
	print(getInput)
	result = getMatched(getInput)
	print(result)
	print('------------')

	getInput = 'abc.di{[]}{@}()[ expected: False'
	print(getInput)
	result = getMatched(getInput)
	print(result)
	print('------------')

	getInput = 'abc.di{ expected: False'
	print(getInput)
	result = getMatched(getInput)
	print(result)
	print('------------')

	getInput = 'abc.di{{( expected: False'
	print(getInput)
	result = getMatched(getInput)
	print(result)
	print('------------')

	getInput = '}}] expected: False'
	print(getInput)
	result = getMatched(getInput)
	print(result)
	print('------------')

	getInput = '({[ expected: False'
	print(getInput)
	result = getMatched(getInput)
	print(result)
	print('------------')




