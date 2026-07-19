from typing import List

def maxArea(height:List) -> int:

    n = len(height)
    most_water = 0

    # Brute Force approach comparing all the values
    # Finding all the possible areas and maximum of it
    # for i in range(n-1):
    #     for j in range(i+1, n):
    #         width = j - i
    #         ht = min(height[i], height[j])
    #         most_water = max(most_water, ht*width)

    # Optimal solution using two pointer approach
    left, right = 0, n-1
    while left < right:
        width = right - left
        ht = min(height[left], height[right])
        most_water = max(most_water, width*ht)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1


    return most_water


if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    print(maxArea(height))
    print(maxArea([1,1]))


