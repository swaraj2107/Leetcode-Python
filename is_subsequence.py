class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = right = 0
        n = len(t)
        m = len(s)

        if(m==0):
            return True

        while(right < n):
            if (s[left]==t[right]):
                left += 1
                right += 1

            else:
                right += 1

            if(left==m):
                return True

        return False
