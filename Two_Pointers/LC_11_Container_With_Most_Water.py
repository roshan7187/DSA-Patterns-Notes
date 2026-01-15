"""
Problem: LC 11 Container With Most Water
Platform: LeetCode
Difficulty: Medium
Pattern: Two Pointers
Link: https://leetcode.com/problems/container-with-most-water/

🧠 Key Insight:
- The amount of water is limited by the **shorter height** of the two lines.
- At each step, calculate the area and **move only the pointer at the shorter line**.
- Keeping the taller line fixed gives the only chance to increase the limiting height.

⚠️ Edge Cases:
- Very small input (length = 2)
- All heights equal
- Heights strictly increasing or strictly decreasing
- Presence of zero height
- Maximum area appearing early in the iteration

❌ Mistake I Made:
- Was confused between taking area with min height with the pointer movement logic.
- Didn’t clearly understand why only the shorter line should be moved.
- Needed iteration-wise dry run to understand pointer movement and why taking the min height is crucial.

🧪 Dry Run:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation:
- The maximum area is formed between heights 8 (index 1) and 7 (index 8).
- Width = 8 - 1 = 7
- Height = min(8, 7) = 7
- Area = 7 × 7 = 49

Solved On: 2026-01-15
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:

        left , right = 0,len(height)-1

        maxarea = 0

        while left <  right :
            w = right - left
            h = min(height[left],height[right])
            area = w * h

            maxarea = max(maxarea,area)

            if height[left] < height[right] :
                left+=1
            else :
                right-=1
        return maxarea