count = 0
total = 0

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
    count = count + 1
    total = total + numberinput
print(" ")
print("Total: ", total)
print("Number of Entries: ", count)
print("Average: ", total/count)
