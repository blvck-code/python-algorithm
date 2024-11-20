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

# * and ** are designed to support functions that take any number of arguments

def f(*args): # python collects all the arguments into a new tuple & assigns the variable args to the tuple
    print(args)

f(1, 2, 3)

def f(**args): # ** form allows you to convert from keywords to dictionaries
    print(args)

f(a=1, b=2)
f(a=1, b=20)


def f(a, *pargs, **kargs): # 1 is passed to a by position, 2 & 3 into pargs positional tuple and x & y into kargs by dict
    print(a, pargs, kargs)

f(1, 2, 3, x=1, y=2)

def func(name='Bob', age=40, job='dev'):
    print(name)

func()

# Unpacking arguments
def func(a, b, c, d):
    print('a =>', a, 'b =>', b,'c =>', c,'d =>', d)

args = (1, 2)
args += (3, 4)
func(*args)

args = {'a': 1, 'b': 2, 'c': 3}
args['d'] = 5
func(**args)

# The complex section
func(*(1, 2), **{'d':4, 'c': 60})
func(1, *(2, 3), **{ 'd': 7 })
func(1, c=3, *(2,), **{'d': 10} )
func(1, *(2, 3), d=4)
func(1, *(2, ), c=3, **{'d': 4})


def kwonly(a, *b, c):
    print(a, b, c)

kwonly(1, 2, c=3) # b collects any extra positional arguments & c must be passed by keyword only
kwonly(1, c=3)

def kwonly(a, *, b, c): # * is to indicate the function does not accept-length argument list but still expects all arguments
    print(a, b, c)      #following the * to be passed as keywords

kwonly(1, c=3, b=2)
kwonly(a=1, c=3, b=2)

def kwonly(a, *, b='spam', c='ham'):       # a may be passed by name or position, and b and c are optional but must be passed if keyword used
    print(a, b, c)

kwonly(1)
kwonly(1, c=3)
kwonly(a=1)
# kwonly(1, 2)



def kwonly(a, *, b, c='ham'): # keyword-only arguments with defaults are optional, but those without defaults
    print(a, b, c)                   # effectively become required keywords for the function

kwonly(1, b='eggs')
# kwonly(1, c='eggs') fails cos b keyword is needed

def kwonly(a, *, b=1, c, d=2):
    print(a, b, c, d)

kwonly(4, c=4) # a and c keyword must be provided


# Ordering rules


















