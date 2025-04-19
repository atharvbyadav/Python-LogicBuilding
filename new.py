list1 = [9,5,4,3,8,5,7]
list2 = [9,5,4,3,8,5,7]

l1 = list1.pop(1)
l2 = list2.pop(5)



string1 = ''.join(str(x) for x in list1)
print("String 1: ",string1)

string2 = ''.join(str(x) for x in list2)
print("String 2: ",string2)

if int(string1) < int(string2):
    print("String 1 is smaller than String 2")
else:
    print("String 2 is smaller than String 1")
