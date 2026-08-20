class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
    
def find_kth_from_end(ll, k):   
    slow = ll.head
    fast = ll.head
    for _ in range(k):
        if fast is None:
            return False
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    return slow
# “Keep a gap of k nodes between fast and slow.”
# "Fast goes k steps ahead, then both walk together until fast ends."
# If fast is k positions ahead of slow, that distance doesn't change when they move together.
# So when: fast = None
# slow must be exactly k positions behind the end. That's why slow points to the kth node from the end.

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = find_kth_from_end(my_linked_list, k)

print(result.value)  # Output: 4