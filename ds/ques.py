"""
Queue is leaner data structure which follows FIFO (First in First out) principle , 
Which means the element which is added first will always be first element to be removed , 
(think of the ordinary checkout line in a store)    


Core operations:
    1) Enqueue - Adds element to the bacl tail of the queue
    2) Dequeue - Removes an element from the front head of the queue
    3) Front / Peek - Displays an element from the front head of the queue
    4) is_empty - checks wether the queue has elements or not 

Tiem complexities:
    1) Enqueue takes O(1) constant time
    2) Dequeue takes O(1) constamt time 
    4) Front / Peek takes O(1) constant time
    5) Searching or accessing by values takes O(n) times,
        because you need to dequeue elements one by one to search by value


"""

class QueElement:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class Queue:
    def __init__(self):
        self.front = None
        self.tail = None
    
    def enqueue(self, value):
        new_el = QueElement(value)
        
        if self.front is None:
            self.front = new_el
            self.tail = new_el
        else:
            self.tail.next = new_el
            self.tail = new_el

    def dequeue(self):
        if self.front is not None:
            raise IndexError("Dequeue cannot be called over empty queue")
        
        dequeued_node = self.front
        self.front = self.front.next
        return dequeued_node.value
    
    