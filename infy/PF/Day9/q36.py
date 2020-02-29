#PF-Prac-36
def find_target_positions(input_string, target_word):
    target_list=[]
    l=list(input_string.split())
    #Start writing your code here
    for i in range(len(l)):
        if(l[i]==target_word):
            if(i not in target_list):
                target_list.append(i)
    #print(target_list)   
    return target_list

def find_inverted_index(input_string):
    #pass
    target_dict={}
    #for i in 
    #Start writing your code here
    for i in input_string:

    
    return target_dict
    
    
input_string="we dont need no education we dont need no thought control no we dont"
result_dict=find_inverted_index(input_string)
print(result_dict)
