print ("Pay Calculator")

hr = input("Enter Hours: ")
rt = input("Enter Rate: ")

try:
    hrs = float(hr)
    rate = float(rt)
except:
    print("Error, please enter numeric input")

if hrs > 40 :
    hrs = hrs - 40
    pay = (40*rate) + (hrs*rate*1.5)
else:
    pay = rate*hrs
print("Pay: ", pay)
