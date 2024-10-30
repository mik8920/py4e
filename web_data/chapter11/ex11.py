# open the file CHECK
# read the file CHECK
# look for integers using re.findall() CHECK
# look for a regular expression of '[0-9]+' CHECK
# convert strings to integers CHECK
# extract the integers CHECK
# sum up the integers CHECK
# sample_data sum = 445833 CHECK
# actual_data sum = ends with 737 CHECK 
#try comprehension CHECK

import re

fileName = input("Enter file name:")

try:
    handleFile = open(fileName)
except:
    print("Invalid file name.")

readFile = handleFile.read()

numbers = re.findall(r"[0-9]+", readFile)

totalSum = 0 
intList = []

for number in numbers:
    if number not in intList:
        intList.append(int(number))

for number in intList:
    totalSum += number
print(totalSum)

#comprehension:
#print(sum([int(number) for number in re.findall('[0-9]+', handleFile.read())]))



