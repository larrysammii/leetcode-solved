"""
1. Two Sum
Easy

Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109

Only one valid answer exists.
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""
from typing import List


# First try, a lot of redundant code as thought processes.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # if the length of list is 2,
        # and given there's always a combination,
        # the answer is always going to be [0, 1].
        if len(nums) == 2:
            return [0, 1]

        # Populate an empty hash map
        hashmap = {}
        for i, num in enumerate(nums):
            hashmap[num] = i
            i += 1

        # Find the difference between the target and num at current loop,
        # if the difference is in the hash map,
        # AND index of the difference != the current loop index ie. j,
        # return the index pair.
        for j in range(len(nums)):
            pair = target - nums[j]
            if pair in hashmap and hashmap[pair] != j:
                return [hashmap[pair], j]


# Second try, thanks NeetCode.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Again, empty hash map
        hashmap = {}
        # Get the key : val in the list.
        for i, num in enumerate(nums):
            # Same same, find the diff.
            pair = target - num
            # If the diff is already in the existing hash map,
            # return the current index, and hash map index.
            if pair in hashmap:
                return [i, hashmap[pair]]

            # Else(e.g. the first loop),
            # map the value as key,
            # index as value.
            else:
                hashmap[num] = i


# Time: O(n)
# Memory: O(n)
