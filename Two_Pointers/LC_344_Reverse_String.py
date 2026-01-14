"""
Problem: LC 344 Reverse String
Platform: LeetCode
Difficulty: Easy
Pattern: Two Pointers
Link: https://leetcode.com/problems/reverse-string/

🧠 Key Insight:
- Use two pointers starting from both ends of the array.
- Swap characters at left and right indices.
- Move pointers inward until they meet.
- This achieves in-place reversal with O(1) extra space.

⚠️ Edge Cases:
- Single character string → no change needed
- Empty list → no operations
- Even vs odd length strings (middle element remains unchanged)

❌ Mistake I Made:
- Initially used `left <= right`, causing an unnecessary self-swap at the middle.
- Returned the array, but the problem requires in-place modification with no return.

🧪 Dry Run:
Input:  ["h","e","l","l","o"]
Step 1: swap h ↔ o → ["o","e","l","l","h"]
Step 2: swap e ↔ l → ["o","l","l","e","h"]
Stop when left >= right

Output: ["o","l","l","e","h"]

Solved On: 2026-01-14
"""

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


# Time Complexity: O(n)
# Space Complexity: O(1)
