# Given a string, I need to find the length of the longest substring that doesn't contain any repeating characters.
# For example, for "abcabcbb", the answer is 3, because of "abc". For "bbbbb", the answer is 1. For "pwwkew",
# the answer is 3, from "wke".

#  Brute force, check all substring O(n^2) and for each substring check the repeatation of letter -> O(n^3)

#  Optimal solution: Sliding window, two pointers start at 0, for each unique letter move the right
#  Store them in Hastmap for easy comparison and increament left if duplicate found to where it found + 1 (no need to compare to that element again)
#  Time O(n) and Space O(n+k), we can reduce space if we know the String is ASCII or lower case letters then reduce space by initailing the array size instead of Hashmap
#  last_seen = [-1] * 128
#  for right, char in enumarate(s):
#       idx = ord(char)
#       if last_seen[idx] > -1:
#           left = last_seen[idx] +1
#       last_seen[idx] = right

def lengthOfLongestSubstring(s:str) -> int:
    last_seen = {}
    left = 0
    max_len = 0

    for right, char in enumerate(s):

        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1

        last_seen[char] = right
        max_len = max(max_len, right - left + 1)

    return max_len


if __name__ == "__main__":
    print(lengthOfLongestSubstring("Sai Krishna"))
    print(lengthOfLongestSubstring("abcabcdab"))
    print(lengthOfLongestSubstring("abcabcbb"))
    print(lengthOfLongestSubstring("bbbb"))
    print(lengthOfLongestSubstring(""))