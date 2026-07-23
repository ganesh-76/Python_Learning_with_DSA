class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def print_linked_list(self):
          temp = self.head
          while temp is not None:
              print(temp.value)
              temp = temp.next


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(6)

my_linked_list.print_linked_list()

print(f'value of head is {my_linked_list.head.value}')
print(f'value of tail is {my_linked_list.tail.value}')
print(f'length is {my_linked_list.length}')