class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if (len(nums)==0):
            return 0

        if (len(nums)==1):
            return nums[0]

        flag=0
        current_sum = nums[0]
        best_sum = nums[0]
        for i in nums[1:]:
            if(i>=0):
                flag+=1
            current_sum = max(i,i+current_sum)
            best_sum = max(best_sum,current_sum)
        
        if(flag>0):
            return best_sum
        else:
            return max(nums)
