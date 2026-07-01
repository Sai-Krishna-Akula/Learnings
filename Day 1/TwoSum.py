
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]


from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        # ## Bruteforce Approach
        # # I will compare all pair of elements of array and check the sum with target and return those indices
        # for i in range(n-1):
        #     total = 0
        #     for j in range(i+1, n):
        #         total = nums[i] + nums[j]

        #         if total == target:
        #             return [i, j]

        # # Optimal solution by storing the elements of array in Hashmap and find the right complement to get the sum to target
        # numMap = {}
        # for i in range(n):
        #     numMap[nums[i]] = i

        # for i in range(n):
        #     complement = target - nums[i]
        #     if complement in numMap and numMap[complement] != i:
        #         return [i, numMap[complement]]

        # return []

        # Optimal solution but storing elements after searching compliment
        numMap = {}

        for i in range(n):
            complement = target - nums[i]

            if complement in numMap:
                return [i, numMap[complement]]
            
            numMap[nums[i]] = i
        
        return []

s1 = Solution()
print(s1.twoSum([2,7,11,15], 9))

print(s1.twoSum([3,2,4], 6))

print(s1.twoSum([3,3], 6))