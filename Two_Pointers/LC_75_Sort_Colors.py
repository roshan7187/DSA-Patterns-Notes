"""
Problem: LC 75 Sort Colors
Platform: LeetCode
Difficulty: Medium
Pattern: Two Pointers
Link: https://leetcode.com/problems/sort-colors/

🧠 Key Insight:
- Maintain three regions using pointers:
  - Left for 0s, middle for 1s, right for 2s.
- Place each element in its correct region in a single pass.
- The middle pointer decides the action at every step.

⚠️ Edge Cases:
- Array with all elements same (all 0s, all 1s, or all 2s)
- Already sorted array
- Reverse sorted array
- Very small input (length 1 or 2)
- Repeated swaps with the high pointer

❌ Mistake I Made:
- Initially thought sorting or counting was required.
- Confused when to increment `mid` after swapping with `high`.
- Forgot that after swapping with `high`, `mid` must be re-evaluated.

🧪 Dry Run:
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Explanation:
- 0s are pushed to the left, 2s to the right, and 1s stay in the middle.
- The array is sorted in a single traversal.

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
