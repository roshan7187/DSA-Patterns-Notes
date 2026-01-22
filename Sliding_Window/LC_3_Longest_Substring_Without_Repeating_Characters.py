"""
Problem: LC 3 Longest Substring Without Repeating Characters
Platform: LeetCode
Difficulty: Medium
Pattern: Sliding Window
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

🧠 Key Insight:
- The substring must contain only unique characters.
- Use a sliding window to maintain a valid substring.
- Expand the window with the right pointer and shrink it from the left when duplicates appear.

⚠️ Edge Cases:
- Empty string
- String with all identical characters
- String with all unique characters
- Single-character string

❌ Mistake I Made:
- Tried restarting the window instead of shrinking it.
- Used `if` instead of `while` to remove duplicates.
- Thought duplicates had to be removed all at once instead of incrementally.
- Confused substring storage with substring length tracking.

🧪 Dry Run:
Input: "abcabcbb"
Output: 3
Explanation:
- Valid longest substrings are "abc", "bca", "cab".
- Each has length 3, which is the maximum.

Solved On: 2026-01-22
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        maxlen = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            maxlen = max(maxlen, right - left + 1)

        return maxlen


# 🟥 Brute Force — How it works (conceptually)
# - Generate all possible substrings.
# - Check each substring for duplicate characters.
# - Track the maximum length of a valid substring.
# - Very slow due to repeated checks.


# 🟨 Better — How it works (conceptually)
# - Fix a starting index.
# - Expand the substring to the right until a duplicate appears.
# - Track the longest valid substring for each start.
# - Avoids some repetition but still quadratic in worst case.


# 🟩 Optimal — How it works (conceptually)
# - Use a sliding window with two pointers.
# - Maintain a set of characters in the current window.
# - Expand the window with the right pointer.
# - Shrink from the left until all characters are unique.
# - Update the maximum window length at each step.
# - Linear time complexity O(n) with constant space for the set.
# - Space complexity O(min(m, n)), where m is the size of the character set and n is the string length.