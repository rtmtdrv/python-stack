class Slist:
    def __init__(self):
        self.head = None
    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.val)
            runner = runner.next
        return self
    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self
    def add_to_back(self, val):
        if self.head == None:
            self.add_to_front(val)
            return self

        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node
        return self

class SLNode:
    def __init__(self, val):
        self.val = val
        self.next = None

my_list = Slist()
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()