# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1
from typing import List
def singleNumber(nums: List) -> int:
    # Bruteforce approach, create a Hashmap and store the elements and increase their count 
    # and return the element which is count one in map
    # numMap = {}
    # for num in nums:
    #     numMap[num] = numMap.get(num, 0) + 1

    # for key,value in numMap.items():
    #     if value == 1:
    #         return key

    # return 0

    # Optimal Solution using XOR, if a number xor with another number result will be zero
    # xor the number with 0 is the number
    # works even number of times numbers got repeated
    result = 0
    for num in nums:
        result ^= num
    return result

if __name__ == "__main__":
    print(singleNumber([2,2,1]))
    print(singleNumber([4,1,2,1,2]))
    print(singleNumber([1]))