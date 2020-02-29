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
        if(self.__head==None):
            self.__head=n
            self.__tail=n
            n.set_data=data
        else:
            temp=self.get_tail()
            temp.set_next(n)
            self.__tail=n
        #Remove pass and write the logic to add an element
    def display(self):
        temp=self.__head
        while(temp!=None):
            print(temp.get_data())
            temp=temp.get_next()
        #Remove pass and write the logic to display the elements
    
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

list1=LinkedList()
list1.add("Sugar")
print("Element added successfully")
#Similarly add all the specified element(s)