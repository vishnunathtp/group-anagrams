# Group Anagrams

High-performance Python solution to group anagrams using frequency key hashing.

## Problem Description
Given an array of strings `strs`, group the anagrams together.

### Example
- Input: `["eat", "tea", "tan", "ate", "nat", "bat"]`
- Output: `[["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]`

## Approach & Complexity
Instead of sorting each string in $O(K \log K)$, build a 26-element character count tuple as the hash map key in $O(K)$ time.

- **Time Complexity:** $O(N \times K)$ where $N$ is word count and $K$ is maximum word length.
- **Space Complexity:** $O(N \times K)$ for hash table groupings.

## How to Run & Test
```bash
python solution.py
python -m unittest discover tests
```
