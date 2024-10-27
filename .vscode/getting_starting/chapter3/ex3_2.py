hoursInput = input("Enter Hours:")
ratePerHourInput = input("Enter Rate Per Hour:")

try:
    hours = float(hoursInput)
    ratePerHour = float(ratePerHourInput)
except:
    print("Error, please enter a numeric input")
    quit()

if hours <= 40:
    grossPay = hours * ratePerHour

else:
    grossPay = (hours - 40) * (1.5 * ratePerHour) + 40 * ratePerHour

print(grossPay)
