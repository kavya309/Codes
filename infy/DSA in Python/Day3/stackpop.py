class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1
    
    def get_max_size(self):
        return self.__max_size
    
    def is_full(self):
        if(self.__top==self.__max_size-1):
            return True
        return False
        #Remove pass and copy the code you had written to check whether stack is full.
    
    def push(self,data):
        if(self.is_full()):
            print("The stack is full")
        else:
            self.__top+=1
            self.__elements[self.__top]=data
        #Remove pass and copy the code you had written to push an element.

    
    def is_empty(self):
        if(self.__top==-1):
            return True
        return False
        #Remove pass and write the logic to check whether stack is empty. If the stack is empty, return true else return false.
    
    def pop(self):
        if(self.is_empty()):
            print("Stack is empty")
        else:
            data=self.__elements[self.__top]
            self.__top-=1
        return data
        #Remove pass and write the logic to pop an element. Pop the element only if stack is not empty. Otherwise, display appropriate message

    def display(self):
        t=self.__top
        while(t>=0):
            print(self.__elements[t])
            t-=1
        #Remove pass and write the logic to display the element(s).
                                              
    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__top
        while(index>=0):
            msg.append((str)(self.__elements[index]))
            index-=1
        msg=" ".join(msg)
        msg="Stack data(Top to Bottom): "+msg
        return msg

stack1=Stack(5)
#Push all the required element(s).
stack1.push(10)
#stack1.display()
stack1.push(20)
#stack1.display()
stack1.push(30)
#Pop an element
print(stack1.pop())
stack1.display()
