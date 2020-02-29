# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
x=set(map(int,input().split()))
m=int(input())
y=list(map(int,input().split()))
p=list(x.difference(y))
print(len(p))
