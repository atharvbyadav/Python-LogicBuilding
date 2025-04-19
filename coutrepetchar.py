s = "Hello World"

count = 0
repeated = []
for char in s:
    if s.count(char) > 1 and char not in repeated:
        count += 1
        repeated.append(char)

print(count)
print(repeated)

