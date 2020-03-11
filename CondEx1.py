print ("Pay Calculator")

hrs = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

if hrs > 40 :
    hrs = hrs - 40
    pay = (40*rate) + (hrs*rate*1.5)
else:
    pay = rate*hrs
print("Pay: ", pay)
