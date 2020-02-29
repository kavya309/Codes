#DSA-Assgn-1

def merge_list(list1, list2):
    #merged_data=""
    #write your logic here
    i=0
    j=0
    l1=[]
    l2=[]
    for item in list1:
        if(item!=None):
            l1.append(item)
            i+=1
    #print(i,l1)
    for item in list2:
        if(item!=None):
            l2.append(item)
            j+=1
    #print(j,l2)
    k=0
    p=[]
    #print(i,j)
    while((k<i) and (j>=1)):
        l=[]
        #if(list1[k] is not None)and (list2[j] is not None):
        l.append(list1[k])
        l.append(list2[j])
        merged_data="".join(map(str, l))
        #print(merged_data.join(str(l)))
        k+=1
        j-=1
        #p.append(merged_data)
    #print(p)
    '''while(k<i):
        l=[]
        l.append(list1[k])
        res=''.join(map(str, l))
        print(res)
        k+=1
    while(j>0):
        l=[]
        l.append(list2[j])
        res=''.join(map(str, l))
        print(res)
        j-=1'''
    #print(str(l))
    #return merged_data

#Provide different values for the variables and test your program
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
merged_data=merge_list(list1,list2)
print(merged_data)s
