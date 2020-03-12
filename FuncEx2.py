print ("Score Classifier")

def computegrade(a):
    if 0.0 <= a <=1.0:
        if a >= 0.9:
            return "A"
        elif a >= 0.8:
            return "B"
        elif a >= 0.7:
            return "C"
        elif a >= 0.6:
            return "D"
        else:
            return "F"
    else:
        return "Invalid score, score out of range"

gr=input("Enter score (0.0-1.0): ")
try:
    grade = float(gr)
except:
    print ("Grade Equivalent: Invalid score, enter a numeric score")

scoreletter = computegrade(grade)
print("Grade Equivalent: ", scoreletter)
