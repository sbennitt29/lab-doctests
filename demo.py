# colors = ["red", "green", "blue"]
# print(colors[-1])

# score = 10
# print(score)
# score += 3
# print(score)
# print(bool(score))

# print(len("automate"))
# print(type(3))

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return not is_even(n)

def absolute_value(x):
    if x < 0:
        return -x
    return x

colors = ["red", "green", "blue", "teal"]

for color in colors:
    print(color)

numbers = [0, 1, 2, 3]

for i in numbers:
    print(i)

for i in range(1, 5):
    print(i)

def factorial(n):
    '''
    Return n!

    >>> factorial(3)
    6
    >>> factorial(5)
    120
    '''
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("the result is:", factorial(5))

