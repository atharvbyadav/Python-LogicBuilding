#Defining function one at a time

# def disp():
#     name = "GeekShows"
#     print("Welcome to", name)

# disp()
# disp()
# disp()


#in python we can use global keyword to change the value of variable

x = 10

def dis():
    global x
    print("Value of x is", x)
    x+=10

dis()
dis()
dis()

#Defining function with parameters

# def add(y):
#     x = 10
#     c = x+y
#     print(c)

# add(20)

def diso():
    def show():
        print("Hello")
    print("Welcome")
    show()

diso()