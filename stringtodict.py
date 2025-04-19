s = "Hello World"

print(s)

words = s.split()

print(words)

new_s = ""

for word in words:
    reversed_word = "".join(reversed(word))
    print(reversed_word)
    swapped_word = reversed_word.swapcase()
    print(swapped_word)
    new_s += swapped_word + " "

print(new_s)

new_s = new_s.rstrip()

print(new_s)
