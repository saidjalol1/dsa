"""
Dynamic arrays:    

Array stores ekemeents in contiguous memory locations.
This allows for fast access to elements using their index, as the memory address can be calculated directly.
However, when the array reaches its capacity and needs to accommodate more elements, 
it must be resized. This resizing process involves creating a new array with a larger capacity, 
copying the existing elements to the new array, and then adding the new element. 
This can lead to performance issues, especially if the array needs to be resized frequently.
    
"""

nums = [1,2,3,5,6]

print(nums[2]) #O(1)



# Dynamic array

class DynamicArray:
    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.data = [None] * self.capacity
        
    def get(self,index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        return self.data[index]
    
    def append(self, value):
        if self.size == self.capacity:
           self.__resize__()
        
        self.data[self.size] = value
        self.size += 1
    
    def __resize__(self):
        self.capacity *= 2
        new_array = [None] * self.capacity
        
        for i in range(self.size):
            new_array[i] = self.data[i]
        
        self.data = new_array