class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        self.index = 0

class DoublyLinkedList:
    def __init__(self, data):
        self.head = Node(data)
        
    def append(self, data):
        current_node = self.head
        node_index = 0
        while current_node.next != None:
            current_node.next.prev = current_node
            current_node = current_node.next
            current_node.index = node_index
            node_index += 1
        current_node.next = Node(data)
        current_node.next.index = current_node.index + 1
        print('done')

    def print(self):
        current_node = self.head
        while current_node != None:
            print(current_node.data)
            current_node = current_node.next
    
    def push(self, data):
        former_head = self.head
        self.head = Node(data)
        self.head.next = former_head
        former_head.prev = self.head
        current_node = self.head
        node_index = 1
        while current_node.next != None:
            current_node.next.index = node_index
            current_node.next.prev = current_node
            current_node = current_node.next
            node_index += 1
        print('done')

    def get_node(self,index):
        current_node = self.head
        while current_node.index != index and current_node.next != None:
            current_node = current_node.next
        return current_node
        
    def insert(self, data, index):
        current_node = self.head
        while current_node.index != index:
            current_node = current_node.next
        former_next_node = current_node.next
        current_node.next = Node(data)
        current_node.next.prev = current_node
        current_node.next.next = former_next_node
        current_node.next.next.prev = current_node.next
        node_index = current_node.index
        print('done')

    def delete(self, index):
        current_node = self.head
        while current_node.index != index and current_node.next != None:
            prev_node = current_node
            current_node = current_node.next  
        prev_node.next = current_node.next
        print('done')

doubly_linked_list = DoublyLinkedList('a')
doubly_linked_list.append('c')
doubly_linked_list.append('d')
doubly_linked_list.append('e')
doubly_linked_list.insert('b',1)
doubly_linked_list.delete(3)

current_node = doubly_linked_list.get_node(3)
print(current_node.data)