class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None

    def get_data(self):
        return self.__data
    
    def set_data(self,data):
        self.__data=data
    
    def get_next(self):
        return self.__next
    
    def set_next(self,next_node):
        self.__next=next_node
    
class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None

    def get_head(self):
        return self.__head
    
    def get_tail(self):
        return self.__tail
    
    def add(self,data):
        n=Node(data)
        if(self.__head is None):
            self.__head=self.__tail=n
        else:
            self.__tail.set_next(n)
            self.__tail=n
        #Remove pass and copy the code you had written to add an element.
    
    def display(self):
        temp=self.__head
        count=0
        while(temp is not None):
            temp=temp.get_next()
            count+=1
        #Remove pass and copy the code you had written to display the element(s).
    
    def find_node(self,data):
        temp=self.__head
        while(temp is not None):
            if(temp.get_data()==data):
                return True
            else:
                temp=temp.get_next()
            return None
            
        #Remove pass and write the logic to find the node and return the node if found or return None.
                                            
    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp=self.__head
        msg=[]
        while(temp is not None):
           msg.append(str(temp.get_data()))
           temp=temp.get_next()
        msg=" ".join(msg)
        msg="Linkedlist data(Head to Tail): "+ msg
        return msg

#nod=Node(10)
list1=LinkedList()
list1.add(10)
list1.add(30)
list1.add(20)
#Add all the required element(s)
#Search for the required node
node=list1.find_node(100)
if(node!=None):
    print("Node found")
else:
    print("Node not found") 
