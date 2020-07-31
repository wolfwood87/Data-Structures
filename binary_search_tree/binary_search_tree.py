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

from stack import Stack
from queue import Queue

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
        else:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        cur_node = self
        while cur_node is not None:
            if target == cur_node.value:
                return True
            elif target > cur_node.value:
                if cur_node.right is None:
                    return False
                else:
                    cur_node = cur_node.right
            else:
                if cur_node.left is None:
                    return False
                else:
                    cur_node = cur_node.left

    # Return the maximum value found in the tree
    def get_max(self):
        cur_node = self
        while cur_node.right is not None:
            cur_node = cur_node.right
        return cur_node.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
        # fn(self.value)
        # cur_node = self
        # stack = # nodes you need to backtrack to
        # while cur_node.left is not None:
        #     cur_node = cur_node.left
        #     fn(cur_node)
        #     #add to the stack
        # # pop off the stack
        # #try to go right
        # while cur_node.right is not None:
        #     cur_node = cur_node.right
        #     fn(cur_node)
            

        
    # def delete(self, value)
    #search like in contains
    # if no children
    # update parent left/right none
    # if 1 child
    # parent.left/right = node.left/right
    # if 2 children
    # larger child becomes parent of its sibling
    # Part 2 -----------------------
    #left, parent, right
    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # if empty
        # if self.left
        # go left with recursion
        #print
        # if self.right
        # go right with recursion
        #
        
        if self:
            if self.left and self.right:
                self.left.in_order_print(self.left)
                print(self.value)
                self.right.in_order_print(self.right)
            elif self.left:
                self.left.in_order_print(self.left)
                print(self.value)
            elif self.right:
                print(self.value)
                self.right.in_order_print(self.right)
            else:
                print(self.value)

                

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(self)
        while queue.__len__() > 0:
            current = queue.dequeue()
            print(current.value)
            if current.left is not None:
                queue.enqueue(current.left)
            if current.right is not None:
                queue.enqueue(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        #create a stack
        stack = Stack()
        stack.push(self)
        while stack.__len__() > 0:
            current = stack.pop()
            print(current.value)
            if current.left is not None:
                stack.push(current.left)
            if current.right is not None:
                stack.push(current.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


bst = BSTNode(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.dft_print(bst)