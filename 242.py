"""
242. Valid Anagram
Easy

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.


Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 1: Check s and t are the same size,
        # if not, return False.
        if len(s) != len(t):
            return False

        # Step 2: Init hash tables for s and t as countS and countT.
        countS, countT = {}, {}

        # Step 3: Looping length of s times, or length of t times, doesn't matter.
        for i in range(len(s)):
            # Step 4: Adding characters to the hash tables (dicts),
            # Keys are the characters,
            # values are the number of times they appear in the string.

            """

                    +---+---+---+---+---+
            key:    | w | q | c |...| e |
                    +---+---+---+---+---+
            value:  | 3 | 5 | 2 |...| 2 |
                    +---+---+---+---+---+

            """

            # Left side meaning:
            # Defining countS's i th key as s's i th character.
            # Right side meaning:
            # Search countS's i th key(the character),
            # getting its i th value(the number of times they appeared).

            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

            # Python's issue: if the hash table (or dict) has no value,
            # simplying calling countS's key will result in key error.
            # Hence, using the .get function

        # Step 5: Loop over hash tables and compare.
        for j in countS:
            if countS[j] != countT.get(j, 0):
                # Meaning: If countS's value at j th key != countT's value at j th key.
                # return False.
                return False
        return True
        # Step 6: Loop close, no difference found, it's an anagram(return True).


# Time: O(n)
# Memory: O(n)
