a = "Wonderful"
num = 3

if len(a) < 6:
    print("no valid input")
else:
    print(a[:num] + a[len(a)-num:])

