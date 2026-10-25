"""

Contains Duplicate II 
You need to return true if any value is repeted within window which has length of k elements
else false
    
"""

array = [12, 23, 45, 67, 89,45, 90]

def contains_duplicate_II(array, k):
    map_vals = set()
    
    for num in range(len(array)):
        
        if num > k:
            map_vals.remove(array[num - k - 1])
            
        if array[num] in map_vals:
            return True

        map_vals.add(array[num])
    
    return False
        

print(contains_duplicate_II(array, 3))