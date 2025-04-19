# # #isalpha fun

# # x = "Atharv Yadav"
# # y = ""

# # for i in x:
# #     if i.isalpha():
# #         y += i

# # print(y)

# # #Take input from user and check if it is a alphanumeric or not

# x = input("Enter the data: ")

# if x.isalnum():
#     print("This is Alphanumeric")
# elif x.isalpha():
#     print("This is Alphabetic")
# elif x.isdigit():
#     print("This is Digit")
# elif x.isspace():
#     print("This is Space")
# else:
#     print("This is not Alphanumeric")



# def disp(st):
#     def show():
#         return "Show function"
#     result = show() + st + " Desp Function"
#     return result

# print(disp("TheCodingCafe"))

# #-------------------------positional arguments--------------------------------

# def add(x,y):
#     z = x**y
#     print(z)
# add(10,20)

#-------------------------keyword arguments--------------------------------

# def add(x,y):
#     z = x+y
#     return z

# def show(name,age):
#     print(f"Name is {name} and age is {age}")

# show(age = input("Enter the age: "),name = input("Enter the name: "))

# def show(name,age=24):
#     print(f"Name is {name} and age is {age}")

# show(input("Enter the name: "))
# #varaible length arguments

def add(*x):
    global c
    global z
    z = x[0]+x[1]+x[2]
    c = print("addition", z, x[3])
    return c
n = input("Enter the number: ")

def num(z):
    while z <= n:
        z += 1
        range.(z)


# add(10,20,30,"zing")
# whie




def add(**num):
    z = num["a"]+num["b"]+num["c"]
    print("Addition:", z)

add(a=10,b=20,c=30)

#keyword variable length arguments menas we can pass any number of arguments to the function and the function will return the addition of the arguments
#varaible length arguments are used to pass the arguments to the function and the function will return the addition of the arguments
#the difference between the variable length arguments is that we can pass the arguments to the function and the function will return the addition of the arguments and variable length arguments are used to pass the arguments to the function and the function will return the addition of the arguments__

#lambda function


x = lambda a,b: a+b
print(x(10,20))

#lambda function is a small anonymous function that can have any number of arguments but can only have one expression
