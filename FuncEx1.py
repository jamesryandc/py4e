print ("Pay Calculator")

def computepay(a, b):
    if a > 40 :
        a = a - 40
        pay = (40*b) + (a*b*1.5)
        return pay
    else:
        pay = a*b
        return pay

hrs = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

total = computepay(hrs, rate)
print("Pay:",total)
