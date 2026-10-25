"""
    

You are given an array , if array consists of any duplicate element you need to return True
else return false    
    
"""


array = [12, 23, 45, 67, 89,45, 90]

def consists_of_duplicate_with_hash_map(array):
    hash_map = {}
    
    for num in range(len(array)):
        if array[num] in hash_map:
            return True
        hash_map[array[num]] = num
        
    return False


def consists_of_duplicate_with_hash_set(array):
    unique = set()
    
    for num in range(len(array)):
        if array[num] in unique:
            return True
        unique.add(array[num])
        
    return False

print(consists_of_duplicate_with_hash_map(array))
print(consists_of_duplicate_with_hash_set(array))