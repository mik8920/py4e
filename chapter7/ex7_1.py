# Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case.

fileName = input('Enter file name:')

openFile = open(fileName, "r")

for line in openFile:
    delLines=line.rstrip()
    readFile = openFile.read()
    print (readFile.upper())