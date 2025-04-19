a = [1,2,3,4,'python','java',7,8,9]

#insert() Method

print("Before inserting: ",a)

a.insert(3, 'c++')

print("After inserting: ",a)

#pop() Method

print("Before popping: ",a)

a.pop()

a.pop(3)

print("After popping: ",a)

#remove() Method

print("Before removing: ",a)

a.remove('python')

print("After removing: ",a)

for elements in a:
    print(elements)

list1 = [9,5,4,3,8,5,7]
list2 = [9,5,4,3,8,5,7]

list1.pop(1)

print("After popping: ",list1)

list2.pop(5)

print("After popping: ",list2)

str1 = ''
for x in list1:
    str1 += str(x)
print("String 1: ",str1)

str2 = ''
for x in list2:
    str2 += str(x)
print("String 2: ",str2)

string1 = ''.join(str(x) for x in list1)
print("String 1: ",string1)

string2 = ''.join(str(x) for x in list2)
print("String 2: ",string2)

if int(string1) < int(string2):
    print("String 1 is smaller than String 2")
else:
    print("String 2 is smaller than String 1")

#clear() Method

# print("Before clearing: ",a)

# a.clear()

# print("After clearing: ",a)

# #append() Method

# list1 = [9,5,4,3,8,5,7]

# list1.append(list2)

# print("After appending: ",list1)

#extend() Method

# list1.extend(list2)

# print("After extending: ",list1)

#nesting a list

list1 = 

#reversing a nested list



