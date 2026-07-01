from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      
        # Bruteforce approach
        n = len(nums)
        max_sum = nums[0]  

        for i in range(n):
            for j in range(i, n):
                total = 0
                for k in range(i, j+1):
                    total = total + nums[k]
                    max_sum = max(total, max_sum)

        return max_sum       

s1 = Solution()
print(s1.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


s2 = Solution()
print(s2.maxSubArray([1]))

s3 = Solution()
print(s3.maxSubArray([5,4,-1,7,8]))

