"""
Stacks is the leaner data structure which followe LIFO principle (Last in , First out)
which means last added element will always be the first to be removed 

Core operations:
    1) push - adds element to the top of the stack and takes O(1) time
    2) pop - removes and returns the element from the top and takes O(1) time as well 
    3) peek / top - displays element from the top element without removing it and takes O(1) time
    4) is_empty - checks wether the stack has elements or not 
    5) accessing the element by value or searching takes O(n) because you need to pop every element to access certain data
    
"""



# Implementation of the Stack
class Stack:
    def __init__(self):
        self.items = []
        
    def push_to_stack(self, data):
        self.items.append(data)
        return
    
    def pop_from_stack(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Pop cannot be called over empty stack")
    
    def top(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Top cannot be called over empty stack")
            
    def is_empty(self):
        return len(self.items) == 0