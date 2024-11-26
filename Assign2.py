"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""
import math
side1 = input("Enter a length for a side")
side2 = input("Enter a length for another side")
ask = input("Is one of these lengths the hypotenuse? (yes or no): ")

if ask == "yes" or ask == "Yes" or ask =="YES":
    if float(side1) / float(side2) < 1:
        #side2 is hypotenuse
        side3 = math.sqrt(float(side2)**2 - float(side1)**2)
        answer = round(side3,1)
        print(answer)
    elif float(side1) / float(side2) > 1:
        #side1 is hypotenuse
        side3 = math.sqrt(float(side1)**2 - float(side2)**2)
        answer = round(side3,1)
    else:
        print("The sides are equal and you lied, neither are the hypotenuse!")
elif ask == "no" or ask == "No" or ask == "NO":
    #side3 is hypotenuse
    side3 = math.sqrt(float(side1)**2 + float(side2)**2)
    answer = round(side3, 1)
    print(answer)
else:
    print("that is not a valid response")
