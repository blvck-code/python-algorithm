# They are not sequences, but instead are mappings.
# Mapping => collections of objects that store objects by key instead of by relative position.
# Dict are mutable, i.e they may change in-place and can grow and shrink on demand, like lists
# Dictionaries are not sequences, they don’t maintain any dependable left-to-right order

D = { 'food': 'Spam', 'quantity': 4, 'color': 'black'  }
print(D['food'])
print(D['quantity'] + 1)

D['quantity'] += 1
print(D)

D = {}
D['name'] = 'Doe'
D['job'] = 'dev'
D['age'] = 40

print(D)
print(D['name'])

# Nesting
rec = { 'name': { 'first': 'Bob', 'last': 'Smith' },
        'job': ['dev', 'mgr'],
        'age': 40.5
        }
print('Name ==>>', rec['name'])
print('Name ==>>', rec['name']['first'], rec['name']['last'])

print('job ==>>', rec['job'][-1]) # Indexing nesting
rec['job'].append('janitor') # Expand Bob's job description in-place
print(rec)

rec = 0
print(rec)
#  Python has a feature known as garbage collection that cleans up
# unused memory as your program runs and frees you from having to manage such details
# in your code. In Python, the space is reclaimed immediately, as soon as the last reference
# to an object is removed

# Step one sorting Dict
D = {'a': 1, 'b': 2, 'c': 3}
print(D)

Ks = list(D.keys())
print(Ks)

Ks.sort()
for key in Ks:
    print(key, '=>', D[key])
# Step 2 sorting Dict


for key in sorted(D):
    print(key, ' => ', D[key])
