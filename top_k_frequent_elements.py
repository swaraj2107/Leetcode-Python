from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        result_map = defaultdict(int)

        for item in nums:
            result_map[item] += 1
        
        result_map = dict(result_map)
        top_n_keys = heapq.nlargest(k, result_map, key=result_map.get)

        return top_n_keys
