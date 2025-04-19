s = "atharv"
new_s = ""

curr_char = 'h'
new_char = 'a'

for char in s:
    if char == curr_char:
        new_s += new_char
    else:
        new_s += char

print(new_s)

new_s = [s[i] if s[i] != curr_char else new_char for i in range(len(s))]
print("".join(new_s))

new_s = s.replace(curr_char, new_char)
print(new_s)

p = "Hello, World!"
comma = ","
dot = "."   
new_p = p.replace(comma, dot)
print(new_p)

new_p = [p[i] if p[i] != comma else dot for i in range(len(p))]
print("".join(new_p))

new_p = [char for char in p if char != " "]
print("".join(new_p))


