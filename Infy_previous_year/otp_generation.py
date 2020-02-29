n=input()
res=""
for i in n:
    #i=int(i)
    if(int(i)%2==0):
        continue
    else:
        res+=str(int(i)**2)       
print(res)
