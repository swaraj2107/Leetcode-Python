from collections import Counter

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_count = Counter()
        prefix_sum_count[0] = 1

        current_prefix_sum = 0
        count = 0

        for i in nums:
            current_prefix_sum += i
            count += prefix_sum_count[current_prefix_sum-k]
            prefix_sum_count[current_prefix_sum] += 1

        return count
