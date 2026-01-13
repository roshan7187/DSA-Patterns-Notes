"""
Problem: LC 26 Remove Duplicates From Sorted Array
Platform: LeetCode
Difficulty: Easy
Pattern: Two Pointers
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

🧠 Key Insight:
- 

⚠️ Edge Cases:
- 

❌ Mistake I Made:
- 

🧪 Dry Run:
Input:
Output:
Explanation:

Solved On: 2026-01-13
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0

        for fast in range(len(nums)) :
            if fast == 0 or nums[fast] != nums[fast-1] :
                nums[slow] = nums[fast]
                slow+=1
        return slow