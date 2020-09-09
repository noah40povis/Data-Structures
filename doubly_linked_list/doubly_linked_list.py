"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    
    def get_next(self):
        return self.next
    
    def set_next(self, new_next):
        self.next = new_next

    def get_prev(self, new_prev):
        self.prev 
    
    def get_value(self):
        return self.prev
    
    def delete(self):
        if self.prev:
            self.prev.next = self.next 
        if self.next: 
            self.next.prev = self.prev
    
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    #you want to make sure you keep modifying the length as you go 
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        #creat a new node 
        new_node = ListNode(value, None, None)
        #add a node 
        self.length += 1
        #is this the first node? 
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            #point to whatever is on the right side 
            new_node.next = self.head
            #pointer to the left 
            self.head.prev =  new_node
            #now make new node the head aka replace the new head 
            self.head = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None:
            return None 
        # set variable value to self
        value = self.head.value
        self.delete(self.head) #delete the value 
        return value #return the value of what was just deleted 
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    #this method is almost identical to the add_head method except
    #change the pointer direction in the else part 
    def add_to_tail(self, value):
        self.length += 1 
        new_node = ListNode(value)
        if not self.tail and not self.head:
            self.head = new_node
            self.tail = new_node
        else: 
            #set self.tail to the old last node using .get_prev 
            new_node.prev = self.tail 
            #use the next function on the old self.tail to creat a new node 
            self.tail.next = new_node
            # se the new node to the new self.tail 
            self.tail = new_node

            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    #the only difference between this and remove_from_head is that this
    # checks if their is self.tail is None: 
    def remove_from_tail(self):
        if self.tail is None: 
            return None 
        value = self.tail.value 
        self.delete(self.tail)
        return value 

            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        #if this the head already then return nothing because it is already the head
        if node is self.head: 
            return 
        value = node.value 
        #if the node is the tail remove from tail then go to the 
        #last line and add value to head 
        if node is self.tail: 
            self.remove_from_tail()
        else: 
            #if the node is somewhere in the middle then delete
            node.delete()
            #delete from length 
            self.length -= 1
            #add node to head 
        self.add_to_head(value)

        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            return 
        value = node.value 
        self.delete(node)
        self.add_to_tail(value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        self.length -= 1 
        #if the function cant do what youre asking to do 
        if self.head is None or node is None:
            return None 
        if self.head == node:
            #apoint a new head
            self.head = node.next 
            node.delete()
        if self.tail == node:
            #appoint a new tail
            self.tail = node.prev 
            node.delete()
        else:
            node.delete()
        
            

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if not self.head:
            return None
        #setting default value to head of list 
        max_val = self.head.value
        #setting current node to the next of the head 
        current_node = self.head.next  
        #while there is a still a current value
        while current_node:
            #if the current value is greater than the current maximum 
            if current_node.value > max_val:
                #replace it 
                max_val = current_node.value
            #go to the next until u find maximum to replace 
            current_node = current_node.next
        
        return max_val