"""
Themes:
    Dynamic arrays / Two pointers:    

        - Array stores ekemeents in contiguous memory locations.
        This allows for fast access to elements using their index, as the memory address can be calculated directly.
        However, when the array reaches its capacity and needs to accommodate more elements, 
        it must be resized. This resizing process involves creating a new array with a larger capacity, 
        copying the existing elements to the new array, and then adding the new element. 
        This can lead to performance issues, especially if the array needs to be resized frequently.
    
        - Two pointers makes most of the O(n 2) operations O(n)
        
        one pointer starts from left , the other from right
        you can use this technique instead of using one loop
        left →            ← right
        [  1,  3,  5,  7,  9  ]

        When Do You Use Two Pointers?

        Use it when you see:
            1. Sorted array
            2. Pair / sum problems
            3. Searching for conditions
            4. Reversing / rearranging
            5. Removing duplicates
     
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
    
    def pop(self):
        if self.size == 0:
            raise IndexError("Empty array")
        
        last_element = self.data[self.size - 1]
        self.data[self.size - 1] = None
        self.size -= 1
        
        return last_element
    
    def __resize__(self):
        self.capacity *= 2
        new_array = [None] * self.capacity
        
        for i in range(self.size):
            new_array[i] = self.data[i]
        
        self.data = new_array
        
    def __str__(self):
        return str(self.data[:self.size])
    
"""Two pointers"""
# Reversing an arrya
array = [1,2,3,4,5,6]

def revers_array(array):
    left = 0
    right = len(array) - 1
    
    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1
        
    return array

print(revers_array(array))


# Remove dublicates 

array_sorted = [1,2,2,2,3,3,3,5,5,5,7,7,7]
def remove_dublicate(array): 
    left = 0

    for  fast in range(1, len(array)):
        if array[left] != array[fast]:
            left += 1
            array[left] = array[fast]
        
    return array

print(remove_dublicate(array_sorted))