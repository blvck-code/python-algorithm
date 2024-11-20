#  it repeatedly executes a block of (normally indented) statements as long
# as a test at the top keeps evaluating to a true value. It is called a “loop” because control
# keeps looping back to the start of the statement until the test becomes false

# while True:
#     print(True)

x = 'spam'
while x:
    print(x, end=' ') #end=' ' keyword argument used here to place all outputs on the same line separated by a space
    # x = x[:-1] # strips string from the last text
    x = x[1:] # strips string from the first text

a = 0; b = 10
while a < b:
    print(a, end=' ')
    a += 1









