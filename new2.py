def pop_element(n):
    listdefaault = [9,5,4,3,8,5,7]
    print(listdefaault)
    listdefaault.pop(n)
    return listdefaault

list1 = pop_element(1)
print(list1)

list2 = pop_element(5)
print(list2)

# list3 = pop_element(3)
# print(list3)

string1 = ''.join(str(x) for x in list1)
print("String 1: ",string1)

string2 = ''.join(str(x) for x in list2)
print("String 2: ",string2)

if int(string1) < int(string2):
    print("String 1 is smaller than String 2")
else:
    print("String 2 is smaller than String 1")
