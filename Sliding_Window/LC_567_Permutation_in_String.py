"""
Problem: LC 567 Permutation in String
Platform: LeetCode
Difficulty: Medium
Pattern: Sliding Window
Link: https://leetcode.com/problems/permutation-in-string/

🧠 Key Insight:
- A permutation is defined by matching character frequencies, not order.
- Fix a window of length len(s1) and slide it over s2.
- If the window’s frequency matches s1’s frequency, a permutation exists.

⚠️ Edge Cases:
- len(s1) > len(s2)
- Exact match at the first window
- Repeated characters in s1
- No valid permutation anywhere in s2

❌ Mistake I Made:
- Compared total character counts of s1 and s2 instead of a substring.
- Returned True/False inside the loop too early.
- Tried checking characters one by one instead of full frequency match.
- Didn’t fix the window size to len(s1).

🧪 Dry Run:
Input:
s1 = "ab", s2 = "eidbaooo"

Output:
True

Explanation:
- Sliding window of size 2 moves over s2.
- Window "ba" has the same character counts as "ab".
- Hence, a permutation exists.

Solved On: 2026-01-22
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = [0] * 26
        window = [0] * 26

        for ch in s1:
            need[ord(ch) - ord('a')] += 1

        for ch in s2[:len(s1)]:
            window[ord(ch) - ord('a')] += 1

        if window == need:
            return True

        left = 0
        for right in range(len(s1), len(s2)):
            window[ord(s2[right]) - ord('a')] += 1
            window[ord(s2[left]) - ord('a')] -= 1
            left += 1

            if window == need:
                return True

        return False


# 🟥 Brute Force — How it works (conceptually)
# - Generate all substrings of s2 with length len(s1).
# - For each substring, sort or count characters.
# - Compare with s1’s sorted form or frequency map.
# - Very slow due to repeated work.


# 🟨 Better — How it works (conceptually)
# - Use a hashmap (Counter) for s1.
# - Slide a fixed-size window over s2.
# - Maintain a hashmap for the window and compare maps.
# - Faster but still involves hashing overhead.
# - O(n) time complexity with O(1) space for the hashmaps.

# 🟩 Optimal — How it works (conceptually)
# - Use a fixed-size array of length 26 (since characters are a–z).
# - Build frequency array for s1 and the first window of s2.
# - Slide the window by adding the right character and removing the left.
# - If both arrays match at any point, return True.
# - O(n) time complexity with O(1) space for the frequency arrays.