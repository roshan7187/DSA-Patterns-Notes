"""
Problem: LC 125 Valid Palindrome
Platform: LeetCode
Difficulty: Easy
Pattern: Two Pointers
Link: https://leetcode.com/problems/valid-palindrome/

🧠 Key Insight:
- The palindrome check must be done using **two pointers**.
- Skip non-alphanumeric characters **on the fly**.
- Compare characters in a **case-insensitive** manner.
- Avoid creating a new string to achieve **O(1) extra space**.

⚠️ Edge Cases:
- Empty string
- String with only special characters (e.g. ".,")
- Mixed case letters (e.g. "Aba")
- Numbers inside the string
- Single-character string

❌ Mistakes I Made:
- Built a new filtered string which used extra space.
- Tried to apply two pointers on an unsorted / unfiltered string incorrectly.
- Used invalid Python syntax (`++`, `--`, `s.[index]`).
- Forgot to initialize `left` and `right` pointers.
- Used variables (`s_left`, `s_right`) before assignment.
- Confused correctness with optimality (extra space used).

🧪 Dry Run:
Input: "A man, a plan, a canal: Panama"
Output: True
Explanation:
- Non-alphanumeric characters are ignored.
- Case is normalized.
- Remaining sequence reads the same forward and backward.

Solved On: 2026-01-15
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if not s[l].isalnum():
            #if not ('a' <= s[l] <= 'z' or '0' <= s[l] <= '9'):
                l += 1
            elif not s[r].isalnum():
            #elif not ('a' <= s[r] <= 'z' or '0' <= s[r] <= '9'):
                r -= 1
            elif s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1

        return True
# Time Complexity: O(n)
# Space Complexity: O(1)