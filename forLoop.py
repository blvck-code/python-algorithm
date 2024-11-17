# The for loop, and its more general cousin the while loop, are the main ways we code
# repetitive tasks as statements in our scripts. Really, though, the for loop (like its relative
# the list comprehension, which we met earlier) is a sequence operation. It works on any
# object that is a sequence and, like the list comprehension, even on some things that are
# not.


# For loop
for c in 'spam':
    print(c.upper())

# While loop
x = 4
while x > 0:
    print('spam!' * x)
    x -= 1


# Iteration and Optimization
squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
print(squares)

squares2 = []
for x in [1, 2, 3, 4, 5]:
    squares2.append(x ** 2)

print(squares2)



