number = 0
total = 0.0

while True:
    userInput = input("Enter number:")

    if userInput == "done":
        break

    try:
        userInputNum = float(userInput)

    except:
        print("Invalid input")
        continue

    number = number + 1
    total = total + userInputNum

print(total, number, total / number)
