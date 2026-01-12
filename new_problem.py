import os
import sys
from datetime import date

if len(sys.argv) != 6:
    print("Usage:")
    print("python new_problem.py <Pattern_Folder> <Platform> <Difficulty> <File_Name> <Problem_URL>")
    sys.exit(1)

pattern = sys.argv[1]
platform = sys.argv[2]
difficulty = sys.argv[3]
file_name = sys.argv[4]
url = sys.argv[5]

folder_path = os.path.join(pattern)
os.makedirs(folder_path, exist_ok=True)

file_path = os.path.join(folder_path, f"{file_name}.py")

if os.path.exists(file_path):
    print("❌ File already exists")
    sys.exit(1)

template = f'''"""
Problem: {file_name.replace("_", " ")}
Platform: {platform}
Difficulty: {difficulty}
Pattern: {pattern.replace("_", " ")}
Link: {url}

🧠 Key Insight:
- 

⚠️ Edge Cases:
- 

❌ Mistake I Made:
- 

🧪 Dry Run:
Input:
Output:
Explanation:

Solved On: {date.today()}
"""

class Solution:
    def solve(self, ...):
        pass
'''

with open(file_path, "w", encoding="utf-8") as f:
    f.write(template)

print(f"✅ Created {file_path}")
