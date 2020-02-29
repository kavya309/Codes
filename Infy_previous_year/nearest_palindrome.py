def n_p(n):
    while True:
        rev=int(str(n)[::-1])
        if rev==n:
            return int(n)
        n+=1
n=int(input())
print(n_p(n))
