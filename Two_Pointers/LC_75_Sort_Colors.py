"""
Problem: LC 75 Sort Colors
Platform: LeetCode
Difficulty: Medium
Pattern: Two Pointers
Link: https://leetcode.com/problems/sort-colors/

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

Solved On: 2026-01-17
"""
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        