# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Example 2:
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      
        # max_sum = nums[0]  
#Brute Force Approach to get the sum of each sum array and find the maximum of it
        # for i in range(n):
        #     total = 0
        #     for j in range(i, n):
        #         total += nums[j]
        #         max_sum = max(max_sum, total)

# Kadane's Algorithm
# An iterative dynamic programming technique used to 
# find the maximum sum of a contiguous subarray within a 1D array of numbers

# The algorithm works by scanning the array while keeping track of two values:
# Current Subarray Sum: The maximum sum of a subarray that ends at the current index. 
# Maximum Sum So Far: The overall maximum sum encountered during the entire traversal.

        max_sum = float('-inf')
        current_sum = 0
        for num in nums:
            current_sum = max(0, current_sum + num)
            max_sum = max(current_sum, max_sum)

        return max_sum       

s1 = Solution()
print(s1.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


s2 = Solution()
print(s2.maxSubArray([1]))

s3 = Solution()
print(s3.maxSubArray([5,4,-1,7,8]))

