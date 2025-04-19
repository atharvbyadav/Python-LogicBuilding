#if else statement

if 5>3:
    print("Greater")
else:
    print("Smaller")


#If Else Statement in a single line(ternary operator)

print("Greater" if 5>3 else "Smaller")

#if else statement with multiple conditions

if 5>3:
    print("Greater")
elif 5==3:
    print("Equal")

#if else statement with multiple conditions in a single line

print("Greater" if 5>3 else "Equal" if 5==3 else "Smaller")

