smallest = "initial"
largest = "initial"

while True:
    num = input("Enter a number: ")
    try:
        numberinput = float(num)
    except:
        if num == 'done':
          break
        else:
          print ('Invalid Input')
          continue
    if smallest == "initial":
        smallest = numberinput
    elif numberinput < smallest:
        smallest = numberinput
    if largest == "initial":
        largest = numberinput
    elif numberinput > largest:
        largest= numberinput
print("")
print("Maximum number:", largest)
print("Minimum number:", smallest)
