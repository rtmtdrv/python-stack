class SLNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class Slist:
    def __init__(self):
        self.head = None

    def addToFront(self, val):
        #create a node w/ given value
        new_node = SLNode(val)
        #set the new node's next to current head
        new_node.next = self.head
        #set the list's head to the new node
        self.head = new_node

x = "hello"
my_list = Slist()
my_list.addToFront("Jim")
my_list.addToFront("Dwight")
my_list.addToFront("Andy")