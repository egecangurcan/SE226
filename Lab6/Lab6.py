from math import factorial

# Task 1

n = int(input("Please enter value for n: "))
x = int(input("Please enter value for x: "))

terms = [n ** i / factorial(i) for i in range(x + 1)]

e = lambda lst: sum(lst)

print(f"The value of e is {e(terms)}")

# Task 2

global result
result = 0


def solver(n):
    global result
    if n == 1:
        result += 1
    else:
        solver(n - 1)
        result += (-1) ** (n + 1) / n


n = int(input("Please enter a number for n: "))

solver(n)
print(result)
