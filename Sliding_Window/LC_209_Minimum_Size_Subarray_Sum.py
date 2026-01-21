"""
Problem: LC 209 Minimum Size Subarray Sum
Platform: LeetCode
Difficulty: Medium
Pattern: Sliding Window
Link: https://leetcode.com/problems/minimum-size-subarray-sum/

🧠 Key Insight:
- All numbers are positive, so the window sum increases when expanded.
- Use a sliding window to expand until the sum reaches the target.
- Shrink from the left to minimize the window length while keeping the sum valid.

⚠️ Edge Cases:
- No subarray reaches the target
- Single element >= target
- Empty array
- Target larger than total array sum

❌ Mistake I Made:
- Used `if` instead of `while` when shrinking the window.
- Used an unsafe sentinel value (`len(nums)`) instead of an impossible value.
- Checked `summ >= target` at the end instead of tracking whether a valid window was ever found.

🧪 Dry Run:
Input: nums = [2,3,1,2,4,3], target = 7
Output: 2
Explanation:
- Valid subarrays with sum ≥ 7 include [2,3,1,2], [3,1,2,4], [4,3].
- The smallest valid subarray is [4,3] with length 2.

Solved On: 2026-01-21
"""

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        summ = 0
        minlen = len(nums) + 1  # sentinel

        for right in range(len(nums)):
            summ += nums[right]

            while summ >= target:
                minlen = min(minlen, right - left + 1)
                summ -= nums[left]
                left += 1

        if minlen == len(nums) + 1:
            return 0
        return minlen


# 🟥 Brute Force — How it works (conceptually)
# - Consider all possible subarrays.
# - Compute the sum of each subarray.
# - Track the minimum length whose sum is ≥ target.
# - Very slow due to repeated sum calculations.


# 🟨 Better — How it works (conceptually)
# - Use prefix sums to compute subarray sums quickly.
# - For each starting index, binary search the smallest ending index
#   such that the subarray sum ≥ target.
# - Improves time but uses extra space and log factor.


# 🟩 Optimal — How it works (conceptually)
# - Use a sliding window with two pointers.
# - Expand the window until the sum reaches the target.
# - Shrink from the left to minimize the window.
# - Track the minimum window length found.
# - Time complexity: O(n), Space complexity: O(1).