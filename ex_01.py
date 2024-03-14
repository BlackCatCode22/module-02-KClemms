hoursWorked = input("Enter Hours: ")
payRate = input("Enter Rate: ")
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
   

