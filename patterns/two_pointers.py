"""
Two pointers is fundamental and vastly used technique in coding interviews,
which is used to process the data structures like (arrays , strings ) in O(n) time
complexity saving you from O(n2) quadratic slow brute force , nested loops
and uses only O(1) constant space complexity

Types of two pointers:
    1) Opposite Endings (Inward-moving pointers) - in thos technique one pointer starts from the beginning of the array
        'left=0' the other starts from the end 'right= len(arr) - 1' and moves towards each other until they meet.
        Usage: sorted arrays, searching pairs which sums to a target, palindrom checking, reversing elements

    2)  Same direction (sliding / chasing pointers) - in this technique both pointers starts from the beginning
        but they move at a different speed and fullfills different conditions (slow pointer and  fast pointer )
        Usage : Removing duplicates , sliding window variations , filtering arrays in place

"""

# Classing two pointer pattern usage
def is_palindrome(s: str):

    # clear string and remove non-alphanumeric chars
    s = " ".join([i.lower() for i in s if i.isalnum()])

    left_pointer = 0
    right_pointer = len(s) - 1
    while left_pointer < right_pointer:
        if s[left_pointer] != s[right_pointer]:
            return {"message": "This is not palindrome string"}

        left_pointer += 1
        right_pointer -= 1

    return True


def two_sum_2nd(arr, target):
    left_pointer = 0
    right_pointer = len(arr) - 1

    while left_pointer < right_pointer:
        current_sum = arr[left_pointer] + arr[right_pointer]

        if current_sum == target:
            return [left_pointer + 1, right_pointer + 1]
        elif current_sum > target:
            right_pointer -= 1
        else:
            left_pointer += 1

    return []


def container_with_most_water(height):
    left_pointer = 0
    right_pointer = len(height) - 1
    max_water = 0

    while left_pointer < right_pointer:
        width = right_pointer - left_pointer
        current_height = min(height[left_pointer], height[right_pointer])
        current_water = width * current_height

        max_water = max(max_water, current_water)

        if height[left_pointer] < height[right_pointer]:
            left_pointer += 1
        else:
            right_pointer -= 1

    return max_water


def three_sum(nums):
    set_ = []
    nums.sort()

    for i in range(len(nums) - 1):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left_pointer = i + 1
        right_pointer = len(nums) - 1
        while left_pointer < right_pointer:
            current_sum = nums[i] + \
            nums[left_pointer] + nums[right_pointer]

            if current_sum == 0:
                set_.append(
                    [nums[i], nums[left_pointer], nums[right_pointer]])
                left_pointer += 1
                right_pointer -= 1
                while left_pointer < right_pointer and nums[left_pointer] == nums[left_pointer - 1]:
                    left_pointer += 1
                while left_pointer < right_pointer and nums[right_pointer] == nums[right_pointer + 1]:
                    right_pointer -= 1

            elif current_sum > 0:
                right_pointer -= 1
            else:
                left_pointer += 1
        return set_
       
 
def sorted_square(nums):
    left_pointer = 0
    right_pointer = len(nums) - 1
    results = [0] * len(nums) 
        
    for i in range(len(nums) - 1, -1 , -1):
        if abs(nums[left_pointer]) > abs(nums[right_pointer]):
            results[i] = nums[left_pointer] ** 2  
            left_pointer += 1
        else:
            results[i] = nums[right_pointer] ** 2
            right_pointer -= 1  

    return results


def move_zeros(nums):
    left_pointer = 0
    right_pointer = 0

    while right_pointer < len(nums):
        if nums[right_pointer] != 0:
            nums[left_pointer], nums[right_pointer] = nums[right_pointer], nums[left_pointer]
            left_pointer += 1
        right_pointer += 1

    return nums


def reverse_vowels(s):
    vowels = set("aeiouAEIOU")
        
    s_list = list(s)
        
    left_pointer = 0
    right_pointer = len(s_list) - 1

    while left_pointer < right_pointer:
        while left_pointer < right_pointer and s_list[left_pointer] not in vowels:
            left_pointer += 1
            
        while left_pointer < right_pointer and s_list[right_pointer] not in vowels:
            right_pointer -= 1
                
        if left_pointer < right_pointer :
            s_list[left_pointer], s_list[right_pointer] = s_list[right_pointer], s_list[left_pointer]
            left_pointer += 1
            right_pointer -= 1 

    return "".join(s_list)


nums = [2,0,2,1,1,0]
def sort_colors(arr):
    white_start = 0
    green_start = len(arr) - 1
    
    iterator = 0
    while iterator <= green_start:
        if arr[iterator] == 0:
            arr[iterator], arr[white_start] = arr[white_start], arr[iterator]
            iterator += 1
            white_start += 1
        elif arr[iterator] == 1:
            iterator += 1
        else:
            arr[green_start], arr[iterator] = arr[iterator], arr[green_start]
            green_start -= 1
        
    return arr
            
print(sort_colors(nums))
