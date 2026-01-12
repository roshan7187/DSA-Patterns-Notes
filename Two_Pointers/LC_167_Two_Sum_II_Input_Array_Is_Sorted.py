"""
Problem: LC 167 Two Sum II Input Array Is Sorted
Platform: LeetCode
Difficulty: Easy
Pattern: Two Pointers
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

🧠 Key Insight:
- Sorted array → use Two Pointer (optimal).

- Unsorted array + only YES/NO or values → sort + Two Pointer.

- Unsorted array + return indices → Hashing (One-Pass Hash Table) is optimal.

- Two Pointer on unsorted array requires storing (value, index) pairs and sorting → not optimal.

⚠️ Edge Cases:
- Duplicate elements (e.g., [3,3])

- Negative numbers

- Target using same value twice

- Large inputs (avoid sorting if possible)

- 0-based vs 1-based indexing

❌ Mistake I Made:
- None

Solved On: 2026-01-12
"""


from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right = 0,len(numbers)-1

        while(left<right):
            
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target :
                return [left+1,right+1]
            elif curr_sum < target :
                left+=1
            else :
                right-=1


