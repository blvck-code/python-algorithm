def min1(*args):
    res = args[0] # 3
    for arg in args[1:]:
        if arg < res:
            res = arg
    return res

def min2(first, *rest):
    for arg in rest:
        if arg <  first:
            first = arg
    return first

def min3(*args):
    tmp = list(args)
    print('tmp ===>>>', tmp)
    tmp.sort()
    return tmp[0]


# print(min1(3, 4, 1, 2))
# print(min2('bb', 'aa'))
# print(min3([2, 2], [1, 1], [3, 3]))
# print(min3(5,4,5,2,1,3))

def mysum(L):
    if not L:
        return 0
    else:
        # return sum(L)
        return L[0] + mysum(L[1:])

print(mysum([1,2,3,4,5]))

def mysum(L):
    return 0 if not L else L[0] + mysum(L[1:])
def mysum(L):
    return L[0] if len(L) == 1 else L[0] + mysum(L[1:])
def mysum(L):
    first, *rest = L
    return first if not rest else first + mysum(rest)

print(mysum([1,2,3,4,5]))

L = [1,2,3,4,5]
sum = 0
while L:
    sum += L[0]
    L = L[1:]
    print(sum)

L = [1,2,3,4,5]
sum = 0
for x in L: sum += x
print(sum)














