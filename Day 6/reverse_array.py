from typing import List

def reverseArray(nums: List) -> List:

    # #  Bruteforce Approach
    # #  Take an duplicate array and store the elements from reverse
    # # Time O(n) and Space O(n)
    # result = []
    # for i in range(len(nums)-1, -1, -1):
    #     result.append(nums[i])

    # for huge array size, having extra array is unnecessary
    # Optimal Solution: Two pointer approach, traverse array from both side
    # swap the ends towards the middle
    # Time O(n) and Space O(1)
    left, right = 0, len(nums)-1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        
        left += 1
        right -= 1
    
    return nums


if __name__ == "__main__":

    print(reverseArray([1, 2, 3, 4, 5]))
    print(reverseArray([]))
    print(reverseArray([-1, -2, -4, -3]))






