from typing import List

def equilibrium_index(nums:List) -> int:

    total_sum = sum(nums)
    left_sum = 0 
    result = []
    for i, num in enumerate(nums):
        right_sum = total_sum - left_sum - num

        if left_sum == right_sum:
            result.append(i)
        
        left_sum += num

    return result


if __name__ == "__main__":
    nums = [-7, 1, 5, 2, -4, 3, 0]
    print(equilibrium_index(nums))
    print(equilibrium_index([0,0,0]))




# # nums = [-7, 1, 5, 2, -4, 3, 0]
# right_sum = total_sum - left_sum - num
# total_sum = 0
# left_sum = -6

# right_sum = 1

