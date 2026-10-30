class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        sorted_array=sorted(nums)
        best_count = seq_count = 1
        prev_num=sorted_array[0]
        for num in sorted_array[1:]:
            if(num == prev_num):
                continue
            elif (num == (prev_num+1)):
                seq_count += 1
                prev_num = num
                best_count = max(best_count,seq_count)
            else:
                seq_count = 1
                prev_num = num
                continue
        return best_count                
