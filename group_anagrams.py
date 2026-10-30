from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = defaultdict(list)
        
        for s in strs:
            key = str(sorted(s))
            anagram_map[key].append(s)
            
        return list(anagram_map.values())
