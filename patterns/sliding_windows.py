"""
Sliding window  pattern is structurally divided into two main variations

1) Fixed sized window - In that pattern the size of the window is fixed ,you slide it step-by step by 
    adding incoming element from right and removing the element from left 

2) Dynamic sized window - The window size can be changed based on a condition or certain constraints 
    
    
"""

# nums = [2,3,1,2,4,3]
# target = 7

# def minimum_subarray(target, nums):
#     left = 0
#     total = 0
#     min_length = float('inf')

#     for right in range(len(nums)):
#         total += nums[right]

#         while total >= target:
#             min_length = min(min_length, right - left + 1)
#             total -= nums[left]
#             left += 1

#     return min_length if min_length != float('inf') else 0
        
        
# print(minimum_subarray(nums=nums, target=7))
        