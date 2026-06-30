# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation:
# The element 1 occurs at the indices 0 and 3.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Explanation:
# All elements are distinct.

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        
        # #Brute force approach, I will travese the complete array for each element
        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         if nums[i] == nums[j]:
        #             return True

        # Optimal solution using HashMap
        numMap = {}
        for i in range(n):
            if nums[i] in numMap:
                return True
            numMap[nums[i]] = i
                
        return False



s1 = Solution()
print(s1.containsDuplicate([1,2,3,1]))

print(s1.containsDuplicate([1,2,3,4]))

assert s1.containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True
