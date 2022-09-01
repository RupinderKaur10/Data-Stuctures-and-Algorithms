heros=['spider man','thor','hulk','iron man','captain america']

l = len(heros)
print(l)
a = heros.append('black panther')
print(heros)
d = heros.remove('black panther')

print(heros)
for i in heros:
    if i == 'hulk':
        heros.insert(3,'black panther')
print(heros)
for i in heros:
    if i == 'thor':
        heros.remove('thor')
        heros.insert(1,'doctor strange')
    if i == 'hulk':
        heros.remove('hulk')
print(heros)
heros.sort()
print(heros)


