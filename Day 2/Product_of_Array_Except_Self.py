# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]


from typing import List
def productOfArray(nums: List) -> list:
    n = len(nums)
    ans = [1]*n

#    # Brute force approach O(n^2)
    # for i in range(n):
    #     x = 1
    #     for j in range(n):
    #         if i != j:
    #             x = x * nums[j]
    #     ans[i] = x
    
    # # prefix and suffix array to multiply each again same of index
    # prefix = [1] * n
    # suffix = [1] * n
    # for i in range(1, n):
    #     prefix[i] = prefix[i-1] * nums[i-1]
    
    # for i in range(n-2, -1, -1):
    #     suffix[i] = suffix[i+1] * nums[i+1]

    # for i in range(n):
    #     ans[i] = prefix[i] * suffix[i]

#  previous approach was costing space of two arrays, let's remove those. 
# instead of storing the resuts, let's directly multiply and store them

    for i in range(1, n):
        ans[i] = ans[i-1] * nums[i-1]

    suffix = 1
    for i in range(n-2, -1, -1):
        suffix *= nums[i+1]
        ans[i] *= suffix

    return ans







if __name__ == "__main__":
    nums = [1,2,3,4]
    print(productOfArray(nums))
    nums = [-1,1,0,-3,3]
    assert productOfArray(nums) == [0, 0, 9, 0, 0]


