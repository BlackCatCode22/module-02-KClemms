# tPythonModule02spr24
tPythonModule02spr24

Post any and all code you completed for Module 02 here!

EXERCISE 3.1

hoursWorked = input("Hours worked: ")
payRate = input("Pay rate: ")
overTimeHrs = float(hoursWorked) - 40
overtimePayRate = float(payRate) * 1.5


if overTimeHrs > 0 :
    OTpay = float(overTimeHrs) * float(overtimePayRate) 
    regularPay = float(payRate) * 40
    totalPay = OTpay + regularPay
    print("$", regularPay, "+ $", OTpay, " = $" ,totalPay)
else:
    totalPay = float(hoursWorked) * float(payRate)
    print("pay: $" ,totalPay)



EXERCISE 3.2

hoursWorked = input("Hours worked: ")
payRate = input("Pay rate: ")
try:
    overTimeHrs = float(hoursWorked) - 40
    overtimePayRate = float(payRate) * 1.5
except: 
    print("Error, please enter numeric input")
    quit()
    
if overTimeHrs > 0 :
    OTpay = float(overTimeHrs) * float(overtimePayRate) 
    regularPay = float(payRate) * 40
    totalPay = OTpay + regularPay
    print("$", regularPay, "+ $", OTpay, " = $" ,totalPay)
else:
    totalPay = float(hoursWorked) * float(payRate)
    print("pay: $" ,totalPay)


EXERCISE 4.6

def computepay(hours, rate) :
    print("In computepay", hours, rate)

    if hours > 40 :
        reg = rate * hours
        otp = (hours - 40.0) * (rate * 0.5)
        pay = reg + otp
    else :
         pay = hours * rate
    print("Returning", pay)
    return pay

sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)

xp = computepay(fh,fr)

print:("Pay:", xp)
