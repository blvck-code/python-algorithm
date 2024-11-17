L = [123, 'spam', 1.23]

# print(len(L))
# print(L[0])
# print(L[:-1])
# print(L + [4, 5, 6])

L.append('NI')
# print(L)
#
# print(L.pop(2))

# M = ['bb', 'aa', 'cc']
#
# M.sort()
# print(M)
#
# M.reverse()
# print(M)
#
# M[2] = 'zzz'
# print(M)

M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# col2 = [row[1] for row in M]
col1 = [row[1] + 10 for row in M]
print('Col 1 ==>>>', col1)

col2 = [row[1] for row in M if row[1] % 2 == 0]
print('Col 2 ===>>>', col2)

diag = [M[i][i] for i in [0, 1, 2]] # Todo do more research
print('Diag ==>>>', diag) # collects diagonals from a Matrix

doubles = [c * 2 for c in 'spam']
print('Doubles ===>>>', doubles)

G = (sum(row) for row in M)
print('Sum row ==>>', next(G))
print('Sum row ==>>', next(G))

l = list(map(sum, M)) #map sum over items in M
print(l)

dict = {sum(row) for row in M}
print('Dict ===>>', dict)  # create a set of row sums

kv = {i: sum(M[i]) for i in range(3)}
print('Key/value ===>>>', kv)

