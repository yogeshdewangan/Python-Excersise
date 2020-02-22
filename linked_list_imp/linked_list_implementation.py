class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        value= self.head
        while value is not None:
            print(value.data)
            value=value.next

    def insert_at_first(self, node):
        node.next=self.head
        self.head= node
        print("Inserted at begning: "+ str(node.data))

    def insert_at_end(self, node):
        next_node= self.head
        while True:
            next_node=next_node.next
            if next_node.next is None:
                next_node.next= node
                print("Inserted at the end: " + str(node.data))
                return

    def insert_after_a_node(self, node_data, new_node):
        next_node = self.head
        while True:
            next_node=next_node.next
            if next_node.data == node_data:
                temp_node =next_node.next
                next_node.next = new_node
                new_node.next=temp_node
                print("Inserted a node after: "+ str(next_node.data))
                return

    def remove(self, data):
        next_node=self.head
        while True:
            previous_node= next_node
            next_node=next_node.next
            if next_node.data == data:
                previous_node.next= next_node.next
                print("Removed: "+ str(data))
                return

    def remove_from_end(self):
        next_node=self.head
        while True:
            previouse_node= next_node
            next_node= next_node.next
            if next_node.next is None:
                previouse_node.next=None
                print("Removed from end: "+ str(next_node.data))
                return


linked_list = LinkedList()
node1= Node(1)
linked_list.head = node1
node2= Node(2)
node1.next = node2
node3= Node(3)
node2.next = node3
linked_list.print()
linked_list.insert_at_first(Node(0))
linked_list.print()
linked_list.insert_at_end(Node(4))
linked_list.print()
linked_list.insert_after_a_node(3, Node(5))
linked_list.print()
linked_list.remove(5)
linked_list.print()
linked_list.remove_from_end()
linked_list.print()



