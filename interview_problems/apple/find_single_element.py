"""
Given an array of integers, arr, where all numbers occur twice except one number which occurs once, find the number. Your solution should ideally be O(n) time and use constant extra space.

Example:
Input: arr = [7, 3, 5, 5, 4, 3, 4, 8, 8]
Output: 7
"""

class Solution(object):
  def findSingle(self, nums):
    xor = nums[0]
    for i in range(1, len(nums)):
      xor = xor ^ nums[i]
    return xor

nums = [1, 1, 3, 4, 4, 5, 6, 5, 6]
print(Solution().findSingle(nums))
# 3