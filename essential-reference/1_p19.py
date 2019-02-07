""" Generator for python3
"""


def countdown(n):
    print("Counting down!")
    while n > 0:
        yield n  # Generate a value (n)
        n -= 1


c = countdown(5)
print(c.__next__())
print(c.__next__())
print(c.__next__())
print(c.__next__())
print(c.__next__())

for i in countdown(5):
    print(i)
