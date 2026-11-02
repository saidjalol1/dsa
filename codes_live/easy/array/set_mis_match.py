
"""


Set mismatch


"""

array = [4,5,3,2,7,6,1,3]

def set_mismatch(array):
    hash_map = {}
    
    for i in range(1, len(array) + 1):
        if array[i] in hash_map and array[i] < 0:
            return [array[i], i]
        
        hash_map[i] = -i
            
    return None
            
print(set_mismatch(array))