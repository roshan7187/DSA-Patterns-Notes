"""
Problem: LC 713 Subarray Product Less Than K
Platform: LeetCode
Difficulty: Medium
Pattern: Sliding Window
Link: https://leetcode.com/problems/subarray-product-less-than-k/

🧠 Key Insight:
- All elements are positive, so the subarray product increases when the window expands.
- A sliding window can be used because the product behaves monotonically.
- For each valid window ending at index `right`, all subarrays starting from `left` to `right` are valid.

⚠️ Edge Cases:
- k <= 1 (no valid subarrays possible)
- Single-element array
- Large numbers causing frequent window shrink
- Array with all elements equal to 1

❌ Mistake I Made:
- Tried to explicitly store subarrays instead of counting them.
- Initialized the window with two pointers instead of starting cleanly.
- Forgot to count subarrays using `right - left + 1`.
- Used floating-point division instead of integer-safe division.
- Placed counting logic outside the valid-window condition.

🧪 Dry Run:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation:
- Valid subarrays:
  [10], [5], [2], [6],
  [10,5], [5,2], [2,6],
  [5,2,6]
- Total count = 8

Solved On: 2026-01-21
"""

from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        left = 0
        prod = 1
        count = 0

        for right in range(len(nums)):
            prod *= nums[right]

            while prod >= k:
                prod //= nums[left]
                left += 1

            count += right - left + 1

        return count


# 🟥 Brute Force — How it works (conceptually)
# - Generate all possible subarrays.
# - Compute the product of each subarray.
# - Count those whose product is strictly less than k.
# - Repeats product computation many times.


# 🟨 Better — How it works (conceptually)
# - Fix a starting index.
# - Extend the subarray to the right while maintaining the product.
# - Stop extending when the product becomes >= k.
# - Repeat for each starting index.
# - Avoids recomputing products from scratch but still nested loops.


# 🟩 Optimal — How it works (conceptually)
# - Use a sliding window with two pointers.
# - Maintain a running product of the window.
# - Expand the window by moving the right pointer.
# - Shrink the window from the left when product >= k.
# - For each valid window ending at `right`, add `right - left + 1` to the count.
# - Time complexity: O(n), Space complexity: O(1)