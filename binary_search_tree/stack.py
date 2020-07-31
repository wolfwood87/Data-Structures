
"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

from singly_linked_list import LinkedList



class Stack:
    def __init__(self):
        self.size = 0
        # self.storage = []
        self.storage = LinkedList()

    def __len__(self):
        # return len(self.storage)
        return self.storage.length

    def push(self, value):
        # self.storage.append(value)
        # return self.storage
        self.storage.add_to_tail(value)
        self.size += 1
        return self.storage

    def pop(self):
        # if len(self.storage) == 0:
        #     return None
        # else:
        #     return self.storage.pop()
        value = self.storage.remove_tail()
        if self.storage.length != 0:
            self.size -= 1
        return value
