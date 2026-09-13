"""

Linked Lists - This is the sequence of nodes stored in non contagious memory locations, 
every node will store the value and the reference to the next node in the sequence     


Core Characteristics:
    1: Non contagious - which means nodes can be stored anywhere in the memory , they are linked by the references(pointers)
    2: No Random access - in Linked list you can not jump straight to the certain element by index like array[5], 
        every time you need to traverse the elemenets starting from the head node to the next node , then next node , by pointers     
   

Time complexities :
1) Accessing or searching certain element : O(n) becouse you need to traverse the chain pointer by pointer 
2) Inserting or deleting at the head of the linked list : O(1) you just need to change the pointer of the Head node 
3) Inserting or deleting from the middle or from the tail : O(n) you need to travers the nodes starting from head node to the certain node
4) Inserting or deleting can be O(1) if you have the reference     
 
 
 
! Important 
1) There is also doubly linked lists. Doubly linked lists takes more memory , 
because every node stores pointers to the next element and to the predecessor element 
2) There is circular linked-lists in which the last node of the list points to the head node 
3) There is also circular-douply linked lists

"""


# Example of the implementation of Linked list 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self,value):
        node = Node(value) # new node 
        
        if self.head is None: # check head existance 
            self.head = node
            return
        
        current_node = self.head  # track the node 
        while current_node.next:  # traverse the nodes pointer by pointer 
            current_node = current_node.next
        
        current_node.next = node
        return