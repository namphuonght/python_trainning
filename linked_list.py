

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None

        if values is not None:
            self.add_multiple_nodes(values)

    def __str__(self):
        return '->'.join([str(node) for node in self])

    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    @property
    def values(self):
        return [node.value for node in self]

    def add_node(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def add_multiple_nodes(self, values):
        for value in values:
            self.add_node(value)

    def add_node_as_head(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.head = Node(value, self.head)
        return self.head


    def insert_at(self, index, value):
        if index<0 or index>len(self):
            raise Exception('Invalid Index')
        
        if index==0:
            self.add_node_as_head(value)
            return 
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(value, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>len(self):
            raise Exception('Invalid Index')

        if index==0:
            self.head = self.head.next
            return
        
        count = 1
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            
            itr = itr.next
            count += 1

