n=int(input())
s=list(input())
print(s)
l=[]
for i in s:
    if i not in l:
        l.append(i)
for i in range(len(s)):
    s.remove(l[i])
    print(s)
