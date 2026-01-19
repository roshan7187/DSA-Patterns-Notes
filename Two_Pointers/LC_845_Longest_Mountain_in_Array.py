"""
Problem: LC 845 Longest Mountain in Array
Platform: LeetCode
Difficulty: Medium
Pattern: Two Pointers
Link: https://leetcode.com/problems/longest-mountain-in-array/

🧠 Key Insight:
- A valid mountain has a strictly increasing part followed by a strictly decreasing part.
- The peak must be greater than its immediate left and right elements.
- Only valid peaks are expanded to measure mountain length.

⚠️ Edge Cases:
- Array length < 3
- Strictly increasing array
- Strictly decreasing array
- Flat segments (equal adjacent values)
- Multiple mountains; return only the longest

❌ Mistake I Made:
- Expanded from every index instead of validating peaks first.
- Compared values directly with the peak instead of adjacent elements.
- Counted length incrementally instead of using index boundaries.
- Started expansion from incorrect indices.
- Considered first and last indices as peaks.

🧪 Dry Run:
Input: [2,1,4,7,3,2,5]
Output: 5
Explanation:
- Valid mountain is [1,4,7,3,2].
- Length is 5, which is the maximum.

Solved On: 2026-01-19
"""

from typing import List

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0

        for i in range(1, n - 1):
            if arr[i - 1] < arr[i] > arr[i + 1]:
                
                left = i - 1
                right = i + 1

                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1

                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1

                ans = max(ans, right - left + 1)

        return ans


# 🟥 Brute Force — How it works (conceptually)
# - For every index i:
#   - Check if it can be a peak.
#   - Expand left to verify strictly increasing sequence.
#   - Expand right to verify strictly decreasing sequence.
#   - Compute mountain length.
# - Return the maximum length found.
# - Repeats expansions multiple times.


# 🟨 Better — How it works (conceptually)
# - Precompute increasing lengths from left to right.
# - Precompute decreasing lengths from right to left.
# - For each index:
#   - If both increasing and decreasing lengths are > 0,
#     compute mountain length as inc[i] + dec[i] + 1.
# - Track the maximum.


# 🟩 Optimal — How it works (conceptually)
# - Iterate through the array to find valid peaks.
# - For each peak:
#   - Expand left while strictly increasing.
#   - Expand right while strictly decreasing.
#   - Compute length using final boundaries.
# - Keep the maximum length found.
