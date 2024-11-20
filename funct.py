def times(x, y):
    return x * y

print(times(3, 5))

# Step 1
def intersect(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res

print(intersect('spam', 'scam'))

# Step 2
res = [x for x in 'spam' if x in 'scam']
print(res)

def func():
    x = 4
    action = (lambda n: x ** n)
    return action

x = func()
print(x(2))

def f(a, b, c):
    print(a, b, c)

f(1, 2, 3)
f(c=1, a=2, b=3)

# Default
def f(a, b=2, c=3):
    print(a, b, c)

f(10)
f(a=1)
f(11, 12)
f(1, 4, 5)
f(1, c=6)

def func(spam, eggs, toast=0, ham=0):
    print((spam, eggs, toast, ham))

# caller must always pass at least 2 arguments to match spam and eggs
func(1, 2)
func(1, ham=1, eggs=2)

def f(*args):
    print(args)

f(1, 2, 3)

def f(**args):
    print(args)

f(a=1, b=2)


def f(a, *pargs, **kargs): # 1 is passed to a by position, 2 & 3 into pargs positional tuple and x & y into kargs by dict
    print(a, pargs, kargs)

f(1, 2, 3, x=1, y=2)


