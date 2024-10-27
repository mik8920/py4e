# Open the file romeo.txt and read it line by line. 
# For each line, split the line into a list of words using the split() method. 
# The program should build a list of words. 
# For each word on each line  to see if the word is already in the list and if not append it to the list. 
# When the program completes, sort and print the resulting words in python sort() order as shown in the desired output. 

fileName = input("Enter file name:")
list = list()

try:
    fileHandler = open(fileName)
except:
    print("There is no such file or directory.")

for line in fileHandler:
    words = line.split()

    for word in words:
        if word not in list:
            list.append(word)


list.sort()
print(list)
