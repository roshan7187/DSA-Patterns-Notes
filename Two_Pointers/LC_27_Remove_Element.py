"""
Problem: LC 27 Remove Element
Platform: LeetCode
Difficulty: Easy
Pattern: Two Pointers
Link: https://leetcode.com/problems/remove-element/

🧠 Key Insight:
- The problem does not require preserving the order of elements.
- Use **same-direction two pointers**:
  - One pointer scans the array.
  - One pointer tracks where the next valid element should be written.
- Maintain the invariant:
  "All elements before the write index are not equal to `val`."

⚠️ Edge Cases:
- Empty array
- Array with all elements equal to `val`
- Array with no occurrence of `val`
- Single-element array
- `val` appearing at the beginning or end

❌ Mistake I Made:
- Overcomplicated the solution using left–right swapping.
- Used multiple conditional branches, making the logic harder to reason about.
- Tried to count `k` while also swapping elements, mixing responsibilities.
- Didn’t realize that LC 27 is a **same-direction two-pointer** problem, not an opposite-direction one.
- Focused on correctness instead of simplicity and clarity.

🧪 Dry Run:
Input: nums = [3,2,2,3], val = 3
Output: 2
Explanation:
- Elements not equal to 3 are written at the front.
- Final array starts with [2,2].
- Remaining elements after index 2 are irrelevant.

Solved On: 2026-01-15
"""
from typing import List

class Solution:
    # ✅ Optimal Solution (Same-direction Two Pointers)
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index


"""
❌ My Earlier Approach (Works but NOT Optimal / Overcomplicated)

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums) - 1
        k = 0

        while left <= right:
            if nums[left] == val and nums[right] != val:
                nums[left], nums[right] = nums[right], nums[left]
                k += 1
                left += 1
                right -= 1
            elif nums[left] != val and nums[right] != val:
                k += 1
                left += 1
            elif nums[left] == val and nums[right] == val:
                right -= 1
            else:
                right -= 1
                left += 1
                k += 1
        return k

Reason this is not optimal:
- Too many conditions
- Harder to reason about correctness
- LC 27 does not need left–right swapping
- Single-pass overwrite is cleaner and expected
"""
