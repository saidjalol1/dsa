"""

You are given an array of integers and target num,
You need to find two nums that add up to the target which is given 

"""


array = [12, 23, 45, 67, 89, 90]

def hash_map_approach(nums, target):
    map_val_index = {}
    
    for num in range(len(array)):
        if target - array[num] in map_val_index:
            return map_val_index[target - array[num]]
        map_val_index[array[num]] = num
    
    return None

print(hash_map_approach(array, 112))