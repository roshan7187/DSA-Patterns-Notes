"""
Problem: LC 42 Trapping Rain Water
Platform: LeetCode
Difficulty: Hard
Pattern: Two Pointers
Link: https://leetcode.com/problems/trapping-rain-water/

🧠 Key Insight:
- Water trapped at any index depends on the maximum height to its left and right.
- The limiting boundary is always the smaller of the two.
- Two pointers allow computing this in one pass without extra space.

⚠️ Edge Cases:
- Empty array or length < 3
- Strictly increasing heights
- Strictly decreasing heights
- All bars of equal height
- Zeros in between taller bars

❌ Mistake I Made:
- Initially thought only the next higher bar mattered.
- Tried local comparisons instead of global boundaries.
- Struggled to understand opposite pointers with max tracking.

🧪 Dry Run:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation:
- Each position stores water based on min(left_max, right_max).
- Total trapped water is accumulated across the array.

Solved On: 2026-01-18
"""

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        water = 0

        while left < right:
            if max_left <= max_right:
                left += 1
                if height[left] < max_left:
                    water += max_left - height[left]
                else:
                    max_left = height[left]
            else:
                right -= 1
                if height[right] < max_right:
                    water += max_right - height[right]
                else:
                    max_right = height[right]

        return water


# 🟥 Brute Force — How it works (conceptually)
# - For every position i:
#   - Find the maximum height to the left of i
#   - Find the maximum height to the right of i
#   - Water at i = min(left_max, right_max) - height[i]
# - Sum this for all positions
# Time Complexity: O(n^2)
# Space Complexity: O(1)

# 🟨 Better — How it works (conceptually)
# - Precompute:
#   - left_max[i] = maximum height from start to i
#   - right_max[i] = maximum height from end to i
# - For every position i:
#   - Water at i = min(left_max[i], right_max[i]) - height[i]
# - Sum this for all positions
# Time Complexity: O(n)
# Space Complexity: O(n)


# 🟩 Optimal — How it works (conceptually)
# - Use two pointers starting from both ends
# - Maintain left_max and right_max
# - At each step:
#   - Process the side with the smaller max
#   - Add water based on that side’s max
# - Continue until pointers meet
# - This avoids extra space and computes in one pass
# Time Complexity: O(n)
# Space Complexity: O(1)