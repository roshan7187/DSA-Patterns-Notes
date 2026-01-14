"""
Problem: LC 977 Squares of a Sorted Array
Platform: LeetCode
Difficulty: Easy
Pattern: Two Pointers
Link: https://leetcode.com/problems/squares-of-a-sorted-array/

🧠 Key Insight:
- Since the input array is sorted, we can use two pointers from both ends to compare
absolute values and build the result array from the end.

As we square the numbers, the largest squares will come from the largest absolute values,
which are located at the ends of the sorted array, so we can fill the result array from the back to the front.

⚠️ Edge Cases:
- All negative numbers
- All positive numbers
- Mixed positive and negative numbers

❌ Mistake I Made:
- forgot to use absolute values when comparing elements at the two pointers.
- for got squaring the numbers before placing them in the result array.

🧪 Dry Run:
Input: {-4, -1, 0, 3, 10}
Output: {0, 1, 9, 16, 100}
Explanation: Squaring each element and sorting gives the result.(brute force way)


Solved On: 2026-01-14
"""

class Solution:

    from typing import List
    def sortedSquares(self, nums: List[int]) -> List[int]:

        n = len(nums)
        res = [0]*n
        left = 0
        right = n-1
        pos = n-1

        while(left<=right):
            if abs(nums[left]) > abs(nums[right]) :
                res[pos] = nums[left] ** 2
                left+=1
            else:
                res[pos] = nums[right] **2
                right-=1
            pos-=1
        return res
