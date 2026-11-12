from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        m, n = len(s), len(p)

        if(m<n):
            return []

        p_map = Counter(p)
        s_map = Counter(s[:n])
        result = []
        
        if(s_map == p_map):
                result.append(0)

        for i in range(n,m):
            s_map[s[i]] += 1
            s_map[s[i-n]] -= 1
            
            if(s_map[s[i-n]]==0):
                del s_map[s[i-n]]

            if(s_map==p_map):
                result.append(i-n+1)

        return result
