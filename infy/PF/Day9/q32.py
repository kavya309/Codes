#PF-Prac-32
def check_squares(number):
    #start writing your code here
    for i in range(1,1000):
        for j in range(1,1000):
            if((i*i)+(j*j))==number:
                return True
    return False
number=5
print(check_squares(number))
