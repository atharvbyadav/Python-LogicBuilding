a = [10,20,30,20,10,90,'GeekyShows',10,30]

unique1 = [i for i in a if a.count(i) == 1]
print(unique1)

#Logic
unique = []
for i in a:
    if a.count(i) == 1:
        unique.append(i)
print(unique)

uni = []
for i in a:
    if i not in a:
        uni.append(i)
print(uni)








