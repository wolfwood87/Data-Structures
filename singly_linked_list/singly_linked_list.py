class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if self.length == 0:
            self.tail = new_node
        self.length += 1

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
        else:
            self.tail.set_next(new_node)
        self.tail = new_node
        self.length += 1

    def remove_head(self):
        if self.head is None:
            return None
        elif self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            self.length -= 1
            return value

    def remove_tail(self):
        if self.tail is None:
            return None
        elif self.head == self.tail:
            value = self.tail.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            value = self.tail.get_value()
            prev_value = self.head
            while prev_value.get_next() is not self.tail:
                prev_value = prev_value.get_next()
            prev_value.set_next(None)
            self.tail = prev_value
            self.length -= 1
            return value

    def contains(self, argvalue):
        headvalue = self.head
        truthvalue = None
        if self.head is None and self.tail is None:
            return truthvalue
        elif headvalue.get_value() == argvalue:
            truthvalue = headvalue.get_value()
            return truthvalue
        else:
            while headvalue != None:
                if headvalue.get_value() == argvalue:
                    truthvalue = headvalue.get_value()
                    headvalue = None
                else:
                    headvalue = headvalue.get_next()
            return truthvalue

    def get_max(self):
        # iterate through elements
        cur_node = self.head
        if cur_node is None:
            cur_max = None
        else:
            cur_max = self.head.get_value()
        while cur_node is not None:
            if cur_node.get_value() > cur_max:
                cur_max = cur_node.get_value()
            cur_node = cur_node.get_next()
        return cur_max