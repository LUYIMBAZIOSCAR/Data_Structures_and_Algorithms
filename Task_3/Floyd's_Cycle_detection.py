# Node class
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # Add a node at the end
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    # Floyd's Cycle Detection
    def has_cycle(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

if __name__ =='__main__':
    list1 = LinkedList()

    list1.append(10)
    list1.append(20)
    list1.append(30)
    list1.append(40)

    print(list1.has_cycle())
