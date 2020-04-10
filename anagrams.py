import itertools
s = input("string: ")
p = input("word: ")
texts=[]
pattern=[]
Str=[]
f=[]

for perm in itertools.permutations(p):
     texts.append("".join(perm))
np=len(p)
for i in s:
    pattern.append(i)
for i in range(len(pattern)):
    Str.append(pattern[i:i+np])
if texts in Str:
    print(True)
for i in Str:
    f.append(''.join(i))
for i in f:
    if i in texts:
        print(f.index(i))
