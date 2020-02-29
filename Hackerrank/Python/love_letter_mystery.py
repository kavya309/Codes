q=int(input())
while(q>0):
    s=input()
    n=len(s)
    if(s==s[::-1]):
        print(0)
    else:
        count=0
        for i in range(len(s)//2):
            left=ord(s[i])
            right=ord(s[(n-1)-i])
            if(left!=right):
                count+=abs(left-right)
        print(count)
    q-=1
