# This is a Node class to represnt an individual element in the LinkedList
class Node:
    def __init__(self,data=None,next=None):
        self.data=data #data can contain intergers, numbers or comlex objects
        self.next=next #This is a pointer to the next element

# This is a LinkedList class
class LinkedList:
    def __init__(self):
         self.head=None #This points to the head of the LinkedList

    # A method to insert a data value at the beginning of a LinkedList
    def insert_at_beginning(self,data):
        node=Node(data,self.head) #creating a node whose next value is the head
        self.head=node # assigning the node to head 

    # A method to print the Linked List
    def print(self):
        if self.head is None: # if the Linked List is blank
            print('Linked List is empty')
            return
        else:# if the Linked List is not blank
            itr=self.head # a temporary variable itr to iterate through elements one by one to print a value in each iteration
            Llistr='' # This is a Linked List string
            while itr: 
                Llistr += str(itr.data) + '-->'# adding data from the string to the Linked List
                itr=itr.next

            print(Llistr)

    # inserting a value at the end of the linked List
    def insert_at_end(self,data):
        if self.head is None: #  checking if the Linked List is blank
            self.head = Node(data,None)
            return
        else:
            itr=self.head # This is a temporary variable to iterate through the Linked List and insert an item at the end.
            while itr.next: #  While itr.next has some value, I will keep on iterating
                itr=itr.next

            itr.next=Node(data,None) #  when itr.next = None then I am at the end hence I create a new node 

    def delete_by_value(self, data):
        if self.head is None: # Checking if the list is empty
            print("Linked List is empty")
            return

        # If the value is in the first node
        if self.head.data == data:
            self.head = self.head.next # This moves the head to the next node
            return
        else:
            itr = self.head # This is a temporary pointer that we use to move through the list

            while itr.next: # Keep moving through the list while there is another node after itr
                if itr.next.data == data: # checking the next node's value to see if it is the one we want to delete
                    itr.next = itr.next.next # skipping the next node's value in oder to delete 
                    return

                itr = itr.next # This moves itr one node forward

            print("Value not found") # The value has not been found 

    # A method to traverse through the Linked List
    def traverse(self):
        if self.head is None:  # Checking if the Linked List is empty
            print("Linked List is empty")
            return
        else:
            itr = self.head  # Start traversal from the first node

            while itr:  # Continue while there is a node to visit
                print(itr.data)  # Visit and display the current node
                itr = itr.next  # Move to the next node

    
    

    

if __name__ =='__main__':
    Ll=LinkedList()
    Ll.insert_at_beginning(5)
    Ll.insert_at_beginning(89)
    Ll.insert_at_beginning(97)
    Ll.insert_at_beginning(1)
    Ll.insert_at_end(90)
    Ll.delete_by_value(5)
    Ll.print()
    Ll.traverse()



    
    # Ll.insert_at_end(79)
    # Ll.insert_at_end(1)
    # Ll.delete_by_value(5)
    
    # Ll.traverse()

        




    
    
        