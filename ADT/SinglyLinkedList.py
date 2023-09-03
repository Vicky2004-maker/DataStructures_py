class Node:
    def __init__(self, dataNode):
        self.data = dataNode
        self.next = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
