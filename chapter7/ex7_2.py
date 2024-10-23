# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form: X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.

fileName = input("Enter file name:")

try:
    openFile = open(fileName, "r")
except:
     print("There is no such file or directory.")

count = 0
total=0.0

for line in openFile:
    line = line.rstrip()

    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    splitLine = line.split(":")[1]
    value = float(splitLine)
    count +=1
    total+=value
    

if count >0:
    average=total/count
    print ("Average spam confidence:", average)

else:
    print("No average spam confidence found.")