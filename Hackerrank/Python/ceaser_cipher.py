n=int(input())
s=input()
k=int(input())
res=""
for i in range(n):
    if(k%26==0):
        res=s
    else:
        if(k>26):
            k=k%26
            if(ord(s[i])+k>=97 and ord(s[i])+k<=122) or (ord(s[i])+k>=65 and ord(s[i])+k<=90):
                res+=chr(ord(s[i])+k)
            elif(ord(s[i])+k)>122:
                res+=chr(ord(s[i])+k-122+96)
            elif(ord(s[i])+k)>90:
                res+=chr(ord(s[i])+k-90+64)
            else:
                res+=s[i]
        else:
            if(ord(s[i])+k>=97 and ord(s[i])+k<=122) or (ord(s[i])+k>=65 and ord(s[i])+k<=90):
                res+=chr(ord(s[i])+k)
            elif(ord(s[i])+k)>122:
                res+=chr(ord(s[i])+k-122+96)
            elif(ord(s[i])+k)>90:
                res+=chr(ord(s[i])+k-90+64)
            else:
                res+=s[i]

print(res)
