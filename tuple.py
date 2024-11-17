# Roughly like a list that cannot be changed—tuples are sequences, like lists, but they are
# immutable, like strings. Syntactically, they are coded in parentheses instead of square
# brackets, and they support arbitrary types, arbitrary nesting, and the usual sequence
# operations


T = (1, 2, 3, 4)
print(type(T))
print(len(T))

T = T + (5, 6) # Concatenation
print(T)

print(T[0])
print(T.index(4)) # Tuple methods: 4 appears at offset 3
print(T.count(2)) # 2 appears once


# Like lists and dictionaries, tuples support mixed types and nesting, but they don’t grow
# and shrink because they are immutable

T = ('spam', 3.0, [11, 12, 13])
print(T[1])
print(T[2][1])


# tuples provide a sort of integrity constraint that is convenient in large programs


