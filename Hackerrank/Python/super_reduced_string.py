s=input()
l=[]
for i in s:
    if i not in l:
        l.append(i)
    else:
        if(l[-1]==i):
            l.pop()
        else:
            l.append(i)
if not l:
    print("Empty String")
else:
    print(''.join(l))
