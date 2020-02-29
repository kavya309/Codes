Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Node:
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
        while(temp is not None):
            print(temp.get_data())
            temp=temp.get_next()
        #Remove pass and copy the code you had written to display the element(s).
    
    def find_node(self,data):
        temp=self.__head
        while(temp is not None):
            if(temp.get_data()==data):
                return temp
            else:
                temp=temp.get_next()
            return None
        #Remove pass and copy the code you had written to find the node containing the element.

    
    def insert(self,data,data_before):
        n=Node(data)
        temp=self.__head
        if(data_before is None):
            if(temp.get_data()==None):
                self.__head=self.__tail=n
            else:
                n.set_next(temp)
                self.__head=n
        else:
            while(temp.get_data()!=data_before):
                temp=temp.get_next()
            link=temp.get_next()
            temp.set_next(n)
            n.set_next(link)
            
        #Remove pass and copy the code you had written to insert an element.
    
    def delete(self,data):
        temp=self.__head
        temp1=self.__head
        if(temp.get_data()==data):
            self.__head=temp.get_next()
        elif(self.__tail.get_data()==data):
            while(temp.get_next()!=None):
                temp1=temp
                temp=temp.get_next()
            temp1.set_next(None)
            self.__tail=temp1
        else:
            while(temp.get_data()!=data):
                temp1=temp
                temp=temp.get_next()
            temp1.set_next(temp.get_next())
                
        #Remove pass and write the logic to delete an element.
                                              
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
list1.add(100)
list1.add(0)
list1.add(90)
#Add all the required element(s)
#Delete the required element.
list1.delete(90)
list1.display()
                                              
                                              
