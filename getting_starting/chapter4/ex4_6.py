hoursInput = input("Enter hours:")
rateInput = input("Enter rate:")

try:
    hours = float(hoursInput)
    rate = float(rateInput)
except:
    quit()


def computepay(hours, rate):
    if hours > 40:
        overHours = hours - 40
        overRate = 1.5 * rate
        overPay = overHours * overRate
        payment = overPay + 40 * rate 
        return payment # (1.5)*(hours-40) + 40*rate
    else:
        payment = hours * rate
        return payment


pay = computepay(hours, rate)
print("Pay", pay)
