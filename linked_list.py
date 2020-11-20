class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.index = 0

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
        
    def append(self, data):
        current_node = self.head
        node_index = 0
        while current_node.next != None:
            current_node = current_node.next
            node_index += 1
        current_node.next = Node(data)
        current_node.next.index = current_node.index + 1

    def print(self):
        current_node = self.head
        while current_node != None:
            print(current_node.data)
            current_node = current_node.next

    def length(self):
        current_node = self.head
        nodes_visited = 1
        while current_node.next != None:
            current_node = current_node.next
            nodes_visited += 1
        return nodes_visited

    def push(self, data):
       former_head = self.head
       self.head = Node(data)
       self.head.next = former_head
       current_node = former_head
       while current_node != None:
           current_node.index += 1
        
    
        

linked_list = LinkedList('b')
linked_list.append('e')
linked_list.append('f')
linked_list.push('a')
assert linked_list.length() == 4, linked_list.length()
assert linked_list.head.index == 0, linked_list.head.index
assert linked_list.head.next.index == 1
assert linked_list.head.next.next.index == 2
assert linked_list.head.next.next.next.index == 3, linked_list.head.next.next.next.index
assert linked_list.get_node(0) == 'a', linked_list.get_node(0)