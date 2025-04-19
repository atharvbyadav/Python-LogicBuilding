s = "atharv"

prefix = "at"

print(s[:len(prefix)] == prefix)

if s.startswith(prefix):
    print("yes")
else:
    print("no")

print(s.startswith(prefix))

suffix = "arv"

print(s[-len(suffix):] == suffix)

if s.endswith(suffix):
    print("yes")
else:
    print("no")

print(s.endswith(suffix))

