#PF-Prac-16
def rotate_list(input_list,n):
    #start writing your code here
    j=0
    output_list=[0]*len(input_list)
    for i in range(len(input_list)):
        if(i<(len(input_list)-n)):
            output_list[i+n]=input_list[i]
        elif(i>=(len(input_list)-n)):
            output_list[j]=input_list[i]
            j+=1
    return output_list

input_list= [1,2,3,4,5,6]
output_list=rotate_list(input_list,4)
print(output_list)
