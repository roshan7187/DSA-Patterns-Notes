"""
Problem: LC 643 Maximum Average Subarray I
Platform: LeetCode
Difficulty: Easy
Pattern: Sliding Window
Link: https://leetcode.com/problems/maximum-average-subarray-i/

🧠 Key Insight:
- The subarray length is fixed to k.
- Instead of recomputing the sum each time, reuse the previous sum.
- Sliding the window by removing one element and adding one element gives O(n) time.

⚠️ Edge Cases:
- All numbers are negative
- k == 1
- Array size equals k
- Large values causing floating-point averages

❌ Mistake I Made:
- Initialized max average as 0, which fails for all-negative arrays.
- Forgot to subtract the left element when sliding the window.
- Incremented the left pointer before updating the running sum.
- Tried computing average before forming a full window.

🧪 Dry Run:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation:
- First window: [1,12,-5,-6] → avg = 0.5
- Second window: [12,-5,-6,50] → avg = 12.75
- Third window: [-5,-6,50,3] → avg = 10.5
- Maximum average is 12.75

Solved On: 2026-01-21
"""

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = sum(nums[:k])
        maxavg = summ / k

        left = 0
        for right in range(k, len(nums)):
            summ += nums[right]
            summ -= nums[left]
            left += 1
            maxavg = max(maxavg, summ / k)

        return maxavg


# 🟥 Brute Force — How it works (conceptually)
# - Consider every subarray of length k.
# - Compute the sum and average for each subarray.
# - Track the maximum average.
# - Recomputes sums repeatedly.


# 🟨 Better — How it works (conceptually)
# - Precompute prefix sums.
# - Use prefix sums to compute each k-length subarray sum in O(1).
# - Track the maximum average.
# - Uses extra space for prefix array.


# 🟩 Optimal — How it works (conceptually)
# - Use a fixed-size sliding window of length k.
# - Maintain a running sum.
# - Slide the window by subtracting the left element and adding the next right element.
# - Update the maximum average at each step.
# - Time complexity: O(n), Space complexity: O(1)