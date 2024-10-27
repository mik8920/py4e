maxNum = None
minNum = None

while True:
    numInput = input("Enter a number: ")

    if numInput == "done":
        break

    try:
        number = int(numInput)
    except:
        print("Invalid input")
        continue

    if minNum is None:
        minNum = number
    elif number < minNum:
        minNum = number

    if maxNum is None:
        maxNum = number
    elif number > maxNum:
        maxNum = number

 

print("Maximum is", maxNum)
print("Minimum is", minNum)
