"""
Problem: LC 15 3Sum
Platform: LeetCode
Difficulty: Medium
Pattern: Two Pointers
Link: https://leetcode.com/problems/3sum/

🧠 Key Insight:
- Fix one element and find pairs for the remaining sum using two pointers.
- Sorting enables controlled pointer movement and duplicate handling.
- Uniqueness of triplets is ensured by skipping duplicate values at the right moments.
- After finding a valid triplet, only the pointer(s) that move need duplicate checks.

⚠️ Edge Cases:
- Array with fewer than 3 elements
- All elements are zero
- No possible triplet summing to zero
- Multiple duplicate values
- Large positive or negative values

❌ Mistake I Made:
- Forgot to handle duplicate triplets initially.
- Used incorrect duplicate check logic for the fixed index.
- Used `break` instead of skipping duplicates.
- Moved both pointers incorrectly or without understanding why.
- Confused correctness with performance optimizations.

        *****************************Final one-line revision takeaway**********************************************

- 3Sum is fundamentally about fixing one value, using two pointers for the rest, 
 and controlling duplicates correctly—not about pointer count.

🧪 Dry Run:
Input: [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]
Explanation:
- After sorting, fix each unique value.
- Use two pointers to find complementary pairs.
- Skip duplicates to avoid repeating triplets.

Solved On: 2026-01-16
"""
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        index = 0
        ans = []
        n = len(nums)
        nums.sort()
        while index < n - 2 :

            left,right = index+1, n-1
            
            if index > 0 and nums[index] == nums[index-1] :
                index+=1
                continue

            while left < right :
                if nums[index] + nums[left] + nums[right] == 0 :
                    triplet = [nums[index] , nums[left] , nums[right]]
                    ans.append(triplet)
                    left+=1
                    right-=1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif nums[index] + nums[left] + nums[right] > 0 :
                    right-=1
                else :
                    left+=1
            index+=1
        return ans