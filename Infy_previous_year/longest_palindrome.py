s=input()
#for i in range(len(s)):
    #for j in range(i,len(s)):
        #a=[s[i:j+1]]
        #print(a)
a=[s[i:j+1] for i in range(len(s)) for j in range(i+1,len(s))]
#print(a)
l=0
out=""
for i in a:
    rev=i[::-1]
    if i==rev and len(i)>l:
        l=len(i)
        out=i
print(out)
           
