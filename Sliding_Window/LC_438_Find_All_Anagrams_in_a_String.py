"""
Problem: LC 438 Find All Anagrams in a String
Platform: LeetCode
Difficulty: Medium
Pattern: Sliding Window
Link: https://leetcode.com/problems/find-all-anagrams-in-a-string/

🧠 Key Insight:
- An anagram is defined by matching character frequencies, not order.
- Fix a window of length len(p) and slide it over s.
- If the window frequency matches p’s frequency, record the starting index.

⚠️ Edge Cases:
- len(p) > len(s) → return []
- Repeated characters in p
- Anagrams appearing back-to-back
- Anagram at index 0

❌ Mistake I Made:
- Checked only the first window and returned early.
- Forgot to slide the window across the entire string.
- Confused index tracking with window movement.
- Compared characters instead of full frequency arrays.

🧪 Dry Run:
Input:
s = "cbaebabacd"
p = "abc"

Output:
[0, 6]

Explanation:
- Substring "cba" at index 0 is an anagram of "abc"
- Substring "bac" at index 6 is an anagram of "abc"

Solved On: 2026-01-23
"""
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        need = [0] * 26
        window = [0] * 26
        ans = []

        # build frequency of p
        for ch in p:
            need[ord(ch) - ord('a')] += 1

        # build frequency of first window
        for ch in s[:len(p)]:
            window[ord(ch) - ord('a')] += 1

        if window == need:
            ans.append(0)

        left = 0
        for right in range(len(p), len(s)):
            window[ord(s[right]) - ord('a')] += 1
            window[ord(s[left]) - ord('a')] -= 1
            left += 1

            if window == need:
                ans.append(left)

        return ans


# 🟥 Brute Force — How it works (conceptually)
# - Generate all substrings of s with length len(p).
# - For each substring, sort or count characters.
# - Compare with p’s sorted form or frequency map.
# - Time complexity is very high due to repeated work.


# 🟨 Better — How it works (conceptually)
# - Use a hashmap (Counter) for p.
# - Slide a fixed-size window over s.
# - Maintain a hashmap for the window and compare maps.
# - Faster than brute force but uses hashing.


# 🟩 Optimal — How it works (conceptually)
# - Use two fixed-size arrays of length 26 (since letters are a–z).
# - Build frequency arrays for p and the current window.
# - Slide the window by adding the right character and removing the left.
# - If both arrays match, record the index.


# -------------------------------
# Counter-based solution (alternative)
# -------------------------------
from collections import Counter

class SolutionCounter:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        need = Counter(p)
        window = Counter(s[:len(p)])
        ans = []

        if window == need:
            ans.append(0)

        left = 0
        for right in range(len(p), len(s)):
            window[s[right]] += 1
            window[s[left]] -= 1

            if window[s[left]] == 0:
                del window[s[left]]

            left += 1

            if window == need:
                ans.append(left)

        return ans


# ❌ Disadvantages of Counter approach
# - Uses hashing → slower than array indexing.
# - Extra overhead for dictionary equality checks.
# - Requires deleting zero-count keys to keep comparisons correct.
# - Not true O(1) space (depends on unique characters).
# - Inferior to 26-array when characters are guaranteed a–z.
