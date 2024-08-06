class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None

class LinkedList:
    # constructor for the linkedList
    def __init__ (self, value):
        new_node = Node(value) 
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print (temp.value)
            temp = temp.next





    # 1 - Append
    def append(self,value):
        new_node = Node(value)
        if self.head is None: # test for the case the list is empty first
            self.head = new_node 
            self.tail = new_node
            
        else:
            self.tail.next = new_node  # 1)this is where it point to the new node
            self.tail = new_node   # 2) now we are setting the actual tail 
        self.length += 1
        return True 

# my_linked_list = LinkedList(1) 
# my_linked_list.append(2)
# my_linked_list.print_list()



    # 2 - Pop 
    def pop(self):
        # 1) If the length is 0
        if self.length == 0:
            return None 
        
        # 2) If the length is 1
        elif self.length == 1:
            to_pop = self.head
            self.head = None 
            self.tail = None 
            self.length -= 1
            return to_pop
        
        # 3) Else if neither conditions are matched :
        else:
            temp = self.head
            pre = self.head

            while (temp.next is not None):
                pre = temp
                temp = temp.next

            self.tail = pre # one before the last node
            self.tail.next = None # now we break off the last node
            self.length -= 1
            return temp
         
# my_linked_list = LinkedList(1)
# my_linked_list.append(2)

# # 2 Items in the list  - Returns 2nd Node
# print(my_linked_list.pop())

# # 1 Items in the list  - Returns 1st Node
# print(my_linked_list.pop())

# # 0 Items in the list  - Returns None
# print(my_linked_list.pop())



    # 3 - Prepend 
    def prepend(self, value):

        new_node = Node(value)

        # 1) If the length is 0
        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        # 2) In the other case where it is not 0     
        else:
            new_node.next = self.head
            self.head = new_node 

        self.length += 1
        return True
    
# my_linked_list = LinkedList(1)
# my_linked_list.append(2)
# my_linked_list.prepend(5)

# Should be 512 as im prepending the 5 
# my_linked_list.print_list()



    # 4 - Pop First 
    def pop_first(self):

        # 1) If the length is 0
        if self.length == 0:
            return None 
        
        # 2) If the length is 1
        elif self.length == 1:
            to_pop = self.head
            self.head = None 
            self.tail = None 
            self.length -= 1
            return to_pop
        
        # 3) Else if neither conditions are matched :
        else:
            temp = self.head 
            self.head = self.head.next 
            temp.next = None
            self.length -= 1
            return temp

# my_linked_list = LinkedList(1)
# my_linked_list.append(2)

# # 2 Items in the list  - Returns 1st Node
# print(my_linked_list.pop_first())

# # 1 Items in the list  - Returns 2nd Node
# print(my_linked_list.pop_first())

# # 0 Items in the list  - Returns None
# print(my_linked_list.pop_first())



    # 5 - Get 
    def get (self, index):

        # 1) If index is out of the range of the length 
        if index < 0 or index >= self.length:
            return None
        
        # 2) In other case : Move temp from head given (index) number of times
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

# my_linked_list = LinkedList(5)
# my_linked_list.append(9)
# my_linked_list.append(7) 
# my_linked_list.append(1)
# print(my_linked_list.get(2))



    # 5 - Set Value 
    def set_value(self, index, value):

        # 1) Setting temp equal to our "4 - Get" 
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False # 2) If the get methods returns None
        
# my_linked_list = LinkedList(5)
# my_linked_list.append(9)
# my_linked_list.append(7) 
# my_linked_list.append(1)
# my_linked_list.print_list()
# print(my_linked_list.set_value(2,5))
# my_linked_list.print_list()



    def insert(self, index, value):

        if index < 0 or index > self.length:
            return None

        out of range 

        they insert at the index of 0 

        insert at the end of the list 









        
        




        


    













        
        


            
       

    




    

    


