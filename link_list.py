class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_next(self):
        return self.next_node
    
    def set_next(self, next_node):
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.get_next():
            last_node = last_node.get_next()
        last_node.set_next(new_node)

    def delete_node(self, key):
        current_node = self.head
        if current_node and current_node.get_data() == key:
            self.head = current_node.get_next()
            current_node = None
            return
        prev_node = None
        while current_node and current_node.get_data() != key:
            prev_node = current_node
            current_node = current_node.get_next()
        if current_node is None:
            return
        prev_node.set_next(current_node.get_next())
        current_node = None

    def search(self, key):
        current_node = self.head
        while current_node:
            if current_node.get_data() == key:
                return True
            current_node = current_node.get_next()
        return False

    def display(self):
        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(current_node.get_data())
            current_node = current_node.get_next()
        print(" -> ".join(map(str, nodes)))

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
