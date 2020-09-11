"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is not None: 
                #running insert on itself is called recursion 
                self.left.insert(value) #by running insert again it , it is starting the process all over again 
            else: #this equals None 
                self.left = BSTNode(value) #therfore turn this to the new left value  
        else: 
            if self.right is not None: 
                self.right.insert(value)
            else: 
                self.right = BSTNode(value)    
        
    #checks to see if a given value is within the tree already  
    def contains(self, target):
        if self.value == target: 
            return True 
        elif target < self.value and self.left is not None:
            return self.left.contains(target)
            #binary search trees can have duplicate values but they must always fall to the right of the original 
        elif target >= self.value and self.right is not None: 
            return self.right.contains(target)
        else: 
            return False


    # Return the maximum value found in the tree
    def get_max(self):
        return self.right.get_max() if self.right is not None else self.value 

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        #start at the root
        fn(self.value)
        if self.left is not None: 
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)

        if self.value: 
            fn(self.value)
            if self.right:
                self.right.for_each(fn)
            if self.left: 
                self.left.for_each(fn)

    #example for the for_each funciton 
    # def subtract(value):
    #     return value*1
    
    # node1 = BSTNode(1)
    # node1.for_each(subtract())
    # node1.insert(2)
    # node1.for_each(subtract())
        

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left is not None:
            self.left.in_order_print()
        print(self.value)
        if self.right is not None:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal. goes down layer by layer . fifo 
    def bft_print(self):
        queue = []
        queue.append(self)
        while len(queue):
            current = queue.pop(0)
            print(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal. goes down one whole leg before going down the next whole leg 
    def dft_print(self):
        stack = []
        stack.append(self)
        while len(stack):
            current = stack.pop()
            print(current.value)
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        if self is not None:
            print(self.value)
            if self.left:
                self.left.pre_order_dft()
            if self.right:
                self.right.pre_order_dft()


    # Print Post-order recursive DFT
    def post_order_dft(self):
        if self is not None:
            if self.left:
                self.left.post_order_dft()
            if self.right:
                self.right.post_order_dft()
            print(self.value)

    def in_order_dft(self):
        if self is not None:
            if self.left:
                self.left.in_order_dft()
            print(self.value)
            if self.right:
                self.right.in_order_dft()

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_dft()
print("post order")
bst.post_order_dft()  
