"""
Problem: LC 2461 Maximum Sum of Distinct Subarrays With Length K
Platform: LeetCode
Difficulty: Medium
Pattern: Sliding Window
Link: https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

🧠 Key Insight:
- The subarray length is fixed to k.
- All elements inside the window must be distinct.
- A sliding window with a set allows enforcing distinctness efficiently.
- The sum is updated incrementally as the window slides.

⚠️ Edge Cases:
- k greater than array length
- Array with all duplicate values
- No subarray of length k with distinct elements
- k == 1
- Large numbers causing sum updates

❌ Mistake I Made:
- Tried controlling the window only using duplicate checks.
- Manually incremented the right pointer inside a for-loop.
- Forgot to update the running sum when adding/removing elements.
- Mixed window-size logic with duplicate-handling logic.
- Computed max sum using incorrect expressions.

🧪 Dry Run:
Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
Explanation:
- Valid distinct subarrays of length 3 are [1,5,4] and [5,4,2].
- Their sums are 10 and 11 respectively.
- The maximum valid sum is 15 from [4,2,9].

Solved On: 2026-01-20
"""

from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        seen = set()
        left = 0
        curr_sum = 0
        max_sum = 0

        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1

            seen.add(nums[right])
            curr_sum += nums[right]

            if right - left + 1 == k:
                max_sum = max(max_sum, curr_sum)
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1

        return max_sum


# 🟥 Brute Force — How it works (conceptually)
# - Consider every subarray of length k.
# - For each subarray:
#   - Check if all elements are distinct.
#   - If yes, compute its sum.
# - Return the maximum sum among all valid subarrays.
# - This repeats checks and summations many times.


# 🟨 Better — How it works (conceptually)
# - Use a sliding window of length k.
# - Maintain a set to track distinct elements.
# - For each window:
#   - If distinctness holds, compute the sum.
# - Still recalculates sums or checks repeatedly.


# 🟩 Optimal — How it works (conceptually)
# - Use a sliding window with two pointers.
# - Maintain a set for distinct elements and a running sum.
# - Shrink the window when duplicates appear.
# - When window size reaches k, update the maximum sum.
# - Slide forward while maintaining all invariants.
#Time Complexity: O(N)
#Space Complexity: O(K)