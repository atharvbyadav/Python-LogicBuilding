s = "atharv"
new_s = ""

for i in range(len(s)):
    if i % 2 != 0:
        new_s += s[i]

print(new_s)

new = [s[i] for i in range(len(s)) if i % 2 != 0]
print("".join(new))

x = "atharv"
n = 2

if len(x) == 0 or len(x) < n:
    print("invalid ")
else:
    new_st = [s[i] for i in range(len(x)) if i != n]
    print("".join(new_st))

if len(x) == 0 or len(x) < n:
    print("invalid input")
else:
    new_st = ""
    for i in range(len(x)):
        if i != n:
            new_st += x[i]
    print(new_st)

