# Leap Year Checker

year = 2004

if (year % 4 == 0) and (year % 100 != 0):
    print("Leap Year")
elif (year % 400 == 0) and (year % 100 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
