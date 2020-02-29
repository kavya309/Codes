s=input()
b=""
for i in range(len(s)):
    if s[i].lower() in b or s[i].upper() in b:
        break
    else:
        b+=s[i]
print(b)
