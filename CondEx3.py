print ("Score Classifier")
gr=input("Enter score (0.0-1.0): ")

try:
    grade = float(gr)
    print (" ")
except:
    print ("Invalid score, enter a numeric score")
if 0.0 <= grade <=1.0:
    if grade >= 0.9:
        print("A")
    elif grade >= 0.8:
        print("B")
    elif grade >= 0.7:
        print("C")
    elif grade >= 0.6:
        print("D")
    else:
        print("F")
else:
    print("Invalid score, score out of range")
