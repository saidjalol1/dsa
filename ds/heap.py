"""
The Heap is specialized tree-based data structure that satisfies the heap property.
A Priority Queue is abstract data type and A heap is the standart underlying sata structure 
used to implement it efficiently 


Min Heap : The value of the each parent node is less or equla to its children
            The minimum element is always at the root O(1) access.

Max-heap : The value of each parent node is larger or equal to its children
            The maximum element is always at the root O(1) access.
            
Core operations:
    1) Peak , Get min/max - The root node is always the target = O(1)
    2) Insert / Push - Adds the element to the end and 'bubbles up' to maintain heap property = O(log n)
    3) Pop - Extract 'Min/Max' the root node then moves the last element to the root , then sinks down to restore order = O(log n)
    4) search by arbitrary value - Heaps are not designed for searching , they are made for fast access to the min and max priority elements = O(n)
    

Python provides heapq module, which implements min-heap using regular python list
you can use in interviews

For Max-Heaps you can just use this heapq module as well but when popping and pushing
you need to multiply numbers by -1 
"""

import heapq

# initialize empty heap (Just standart python list)

min_heap = []

# push elements to the heap , O(log n)
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 4)
heapq.heappush(min_heap, 15)
heapq.heappush(min_heap, 1)

print("Minimum element is always at the 0th elemement :", min_heap[0]) # Output 1

# Pop minimum element O(log n)
smallest = heapq.heappop(min_heap)
print("Popped element: ", smallest) #Output 1
print("New min element: ", min_heap[0]) #Output 4
