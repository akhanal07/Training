class Node:
    def _init_(self,value):
        self.value = value
        self.next = None


class LinkedList:
    
    def _init_(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self,value): 
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

obj = LinkedList()