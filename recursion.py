def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))

def sum_numbers(n):
    if n == 0:
        return 0
    else:
        number = sum_numbers(n-1)
        return number + n

string = sum_numbers(10)
print(string)

def print_numbers(n):
    if n == 0:
        return 0
    else:
        number = print_numbers(n-1)
        return str(number) + str(n)

string = print_numbers(10)
print(string)


def count_down(n):
    if n == 0:
        print("Blast off!")
    else:
        print(n)
        count_down(n-1)

count_down(10)

li = [1, 2, 3, 4, 5]

def sum_li(li):
    if len(li) == 0:
        return 0
    else:
        return li[0] + sum_li(li[1:])

print(sum_li(li))

# def sum_list(li):
#     if len(li) == 0:
#         return 0
#     else:
#         x = len(li)
#         return li[0] + sum_list(x)

# print(sum_list(li))

def count_down(n):
    if n > 10:
        print("Blast off!")
        return 0
    else:
        print(n)
        return n + count_down(n+1)

count_down(1)