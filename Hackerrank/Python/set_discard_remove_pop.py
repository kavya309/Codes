n = int(input())
s = set(map(int, input().split()))
p=int(input())
while(p):
    x,y=input().split()
    y=int(y)
    if(x=='remove'):
        s.remove(y)
    elif(x=='discard'):
        s.discard(x)
    elif(x=='pop'):
        s.pop(y)
print(s)
