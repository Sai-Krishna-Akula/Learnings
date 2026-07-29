
# Given integer array nums and integer target, we need to return the indices of the array that add up to target
#  Exactly one solution and no element is used twice

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    # Brute force: Straight forward solution is finding the pairs that add up sum as target
    # for i in range(n):

    #     for j in range(i+1, n):

    #         if nums[i] + nums[j] ==  target:
    #             return [i, j]
    # return 0

    # Optimal solution: Storing the elements in Hashmap and find the complement of each element
    # Average time to find element in HashMap is O(1) and Time O(n), Space O(n)
    numsMap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in numsMap:
            return [numsMap[complement], i]

        numsMap[num] = i
    return


if __name__ == "__main__":
    print(twoSum([2, 7, 11, 15], 9))
    print(twoSum([10, -5, -2, 5], 0))
    print(twoSum([3, 3], 6))