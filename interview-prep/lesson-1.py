"""
Lesson 1 : Big O and Why interviewers Care?
    - Before diving into any data - structure, we must learn how to measure efficiency.


    - Interviewers just don't care wether your code works or not 
        - They care:
            - Does it work? 
            - is it fast enough? 
            - Does it use too much memory? 
    
    
"""

#  Imagine this - You have a kist of 10 numbers
nums = [1, 2, 34, 56, 7, 12, 1, 2,5,6]
# You want to find number 12

# One approach 
for num in nums:
    if num == 12:
        print("Found !")
        
# Worst case ? 
# You check every item 
# for 10 nums = 10 operations
# for 10000 nums = 10000 operations

# this is calles O(n) = leaner time

"""
What does O(n) means?     
It means:
    - If input size doubles, work roughly doubles.

Input      Operations
10         10
20         20 
30         30 
40         40 

O(1) - Constant time

"""

# O(1)
nums = [5,6,8]
print(nums[1]) # python instantly knows where index 1 is.
# wether the list have 3000 or 10 billion elements ,the look up costs the same.


"""
O(n2) - Dangerous
    
in this scenario if n = 10 , operations will be 10 x 10  = 100

the formula is n x n 

to find ceratain number in leaner techniqe can take up at worst case n x n time 


"""

for i in nums:
    for j in nums:
        print(i, j)


"""
O(log n) - Extremaly Powerful

In that time complexity , every step removes half of the search space
    
"""

num = [1,2,3,4,5,6,7,8,9,10]


"""
O(n log n)    

"""