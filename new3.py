def pop_element(n, p):
    listdefaault = [9,5,4,3,8,5,7]
    print("Original list:", listdefaault)
    
    if p == 1:
        listdefaault.pop(n)
        return listdefaault, listdefaault.index(n)
    elif p == 0:
        return listdefaault.index(n)

# def index_element(a):
#     listdefaault = [9,5,4,3,8,5,7]
#     return listdefaault.index(a)

b = int(input("Do you want to pop an element or find its index? (1/0): "))
if b == 1:
    c = int(input("Enter the index of the element to be popped: "))
    result = pop_element(n = c, p = 1)
    print("After popping:", result)
else:
    a = int(input("Enter the element to find its index: "))
    index = pop_element(n = a, p = 0)
    print("Index of element:", index)

# list = pop_element(a)
# print(list)

# list3 = pop_element(3)
# print(list3)

# string1 = ''.join(str(x) for x in list1)
# print("String 1: ",string1)

# string2 = ''.join(str(x) for x in list)
# print("String 2: ",string2)

# if int(string1) < int(string2):
#     print("String 1 is smaller than String 2")
# else:
#     print("String 2 is smaller than String 1")
