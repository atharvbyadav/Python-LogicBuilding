def check(string,substring):
    i = 0
    j = 0
    while i < len(string) and j < len(substring):
        if string[i] == substring[j]:
            j+=1
        i+=1
    return j == len(substring)

string = "atharvyadav"
substring = "arv"
result = check(string,substring)
print(result)

# if substring in string:
#     print("substring is present")
# else:
#     print("substring is not present")
