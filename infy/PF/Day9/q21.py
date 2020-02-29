#PF-Prac-21
def check_numbers(num1,num2):
    num_list=[]
    #start writing your code here
    for i in range(num1,num2+1):
        for j in range(num1,num2+1):
            if(i%j==0 and i!=j):
                num_list.append(i)
    count=len(num_list)
    s=set(num_list)
    return [s,count]

num1=10
num2=30
print(check_numbers(num1, num2))
