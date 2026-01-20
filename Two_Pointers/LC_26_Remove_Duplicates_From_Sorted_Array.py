"""
Problem: LC 26 Remove Duplicates From Sorted Array
Platform: LeetCode
Difficulty: Easy
Pattern: Two Pointers
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

🧠 Key Insight:
- Since the array is already sorted, duplicates are always adjacent.
- Use two pointers to overwrite duplicates in-place while maintaining order.
- The slow pointer tracks the position of the next unique element.

⚠️ Edge Cases:
- Array with length 0 or 1
- All elements are the same
- No duplicates at all
- Large array with many repeated values

❌ Mistake I Made:
- Initially thought extra space or a set was required.
- Forgot that sorted order guarantees duplicates are adjacent.
- Tried unnecessary swapping instead of simple overwriting.

🧪 Dry Run:
Input: [0,0,1,1,1,2,2,3,3,4]
Output: 5
Explanation:
- Unique elements are [0,1,2,3,4].
- First 5 positions of the array are overwritten with these values.

Solved On: 2026-01-13
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0

        for fast in range(len(nums)):
            if fast == 0 or nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1

        return slow


# 🟥 Brute Force — How it works (conceptually)
# - Iterate through the array.
# - For each element, check if it already appeared before.
# - If duplicate, remove it by shifting elements left.
# - Repeated shifting makes this inefficient.


# 🟨 Better — How it works (conceptually)
# - Use an auxiliary data structure (like a set) to track seen elements.
# - Copy only unique elements back into the array.
# - Improves time but uses extra space.


# 🟩 Optimal — How it works (conceptually)
# - Use two pointers on the sorted array.
# - Fast pointer scans the array.
# - Slow pointer tracks position for next unique element.
# - Overwrite duplicates in-place and return the count of unique elements.
