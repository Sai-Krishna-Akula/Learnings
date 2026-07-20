# 15. 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

from typing import List
def three_sum(nums: List[int]) -> List[list[int]]:
    # result is set to remove the duplicates after sorting and storing as set
    result = set()
    n = len(nums)

    #  Bruteforce approach to find the solution: O(n^3)

    # for i in range(n-2):
    #     for j in range(i+1, n-1):
    #         for k in range(j+1, n):

    #             if nums[i] + nums[j] + nums[k] == 0:
    #                 # tuple is immutable and we can add to set and the hash value will be calculated to      
    #                 # if pass list which is mutable and set won't allow it 
    #                 triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
    #                 result.add(triplet)

# Better solution using Hash set
    for i in range(n):

        for j in range(i+1, n):
            complement = -(nums[i]+nums[j])

            if complement in result:
                triplet = tuple(sorted(nums[i], nums[j], complement))
                result.add(triplet)


            




    return [list(t) for t in result]

if __name__ == "__main__":
    print(three_sum([-1,0,1,2,-1,-4]))
    print(three_sum([0,1,1]))
    print(three_sum([0,0,0]))