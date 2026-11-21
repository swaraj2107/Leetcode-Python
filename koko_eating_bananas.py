import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left + right) // 2
            
            hours_needed = sum(math.ceil(p / mid) for p in piles)
            
            if hours_needed <= h:
                right = mid
            
            else:
                left = mid + 1
                
        return left
