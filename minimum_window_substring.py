from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        target = Counter(t)
        required = len(target)
        left, right = 0, 0
        best = float('inf'), -1, -1 

        while right < len(s):
            if s[right] in target:
                target[s[right]] -= 1
                if target[s[right]] == 0:
                    required -= 1

            while required == 0:
                if right - left + 1 < best[0]:
                    best = (right - left + 1, left, right)

                if s[left] in target:
                    target[s[left]] += 1
                    if target[s[left]] > 0:
                        required += 1

                left += 1

            right += 1

        start, end = best[1], best[2]
        return s[start:end + 1] if best[0] != float('inf') else ""
