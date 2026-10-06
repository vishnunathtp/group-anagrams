from typing import List, Dict
from collections import defaultdict

def group_anagrams(strs: List[str]) -> List[List[str]]:
    groups: Dict[tuple, List[str]] = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        groups[tuple(count)].append(s)
    return list(groups.values())

if __name__ == "__main__":
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print("Grouped anagrams:", group_anagrams(words))
