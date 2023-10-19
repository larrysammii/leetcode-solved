""" 
217. Contains Duplicate
Easy

Given an integer array nums, 
return true if any value appears at least twice in the array, 
and return false if every element is distinct. 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109 
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Use hashset, Python's set() function.
        # Check if integer is in hashset,
        # if yes return True,
        # if not add integer to hashset.
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            else:
                hashset.add(num)


# Time: O(n)
# Memory: O(n)
