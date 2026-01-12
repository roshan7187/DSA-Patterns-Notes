import os

BASE_README = """# {emoji} {pattern} Pattern

## 🧩 When to Use
- 

## 🧠 Core Idea
- 

## 🔄 Variants
- 

## ⚠️ Common Mistakes
- 

## ⏱ Complexity
- Time:
- Space:

## ✅ Problems
- 
"""

PATTERNS = {
    "Two_Pointers": ("🔁", "Two Pointers"),
    "Fast_Slow_Pointers": ("🐢🐇", "Fast & Slow Pointers"),
    "Sliding_Window": ("🪟", "Sliding Window"),
    "Kadane": ("📈", "Kadane"),
    "Prefix_Sum": ("➕", "Prefix Sum"),
    "Merge_Intervals": ("🧩", "Merge Intervals"),
    "Cyclic_Sort": ("🔄", "Cyclic Sort"),
    "Inplace_Reversal_LL": ("🔃", "In-Place Reversal (Linked List)"),
    "Stack": ("📚", "Stack"),
    "Hash_Map": ("🗂", "Hash Map"),
    "Binary_Search": ("🔍", "Binary Search"),
    "BFS": ("🌊", "Breadth First Search"),
    "Island": ("🏝", "Island / Matrix Traversal"),
    "Two_Heaps": ("⚖️", "Two Heaps"),
    "Subsets": ("🧮", "Subsets"),
    "Bitwise_XOR": ("❌", "Bitwise XOR"),
    "Top_K": ("🏆", "Top K Elements"),
    "K_Way_Merge": ("🔀", "K-Way Merge"),
    "Greedy": ("🎯", "Greedy"),
    "Knapsack_01": ("🎒", "0/1 Knapsack"),
    "Backtracking": ("🔁", "Backtracking"),
    "Trie": ("🌳", "Trie"),
    "Topological_Sort": ("🧭", "Topological Sort"),
    "Union_Find": ("🔗", "Union Find"),
    "Ordered_Set": ("📐", "Ordered Set"),
}

for folder, (emoji, name) in PATTERNS.items():
    os.makedirs(folder, exist_ok=True)
    readme_path = os.path.join(folder, "README.md")

    if not os.path.exists(readme_path):
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(BASE_README.format(emoji=emoji, pattern=name))

print("✅ All pattern folders & README.md files created")
