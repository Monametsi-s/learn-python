class Node:
    """Setting a template for nodes"""
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

def __str__(self):
    """methods so that we can test the basic mechanism of
      creating and displaying the new type"""
    return str(self.cargo)

node = Node("test")
#print(node.next)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3

#print(node2.next)

def print_list(node):
    while node is not None:
        print(node.cargo, end=" ")
        node = node.next
    print()

print_list(node1)

