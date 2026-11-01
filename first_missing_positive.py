class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        
        for i in range(n):
            val = abs(nums[i])
            if 1 <= val <= n:
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
        
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        
        return n + 1


# class Solution:
#     def firstMissingPositive(self, nums: list[int]) -> int:
#         max_num = len(nums)
#         if(max_num==0):
#             return 1

#         # elif(max_num==1):
#         #     return 2

#         else:
#             for i in range(1,max_num+1):
#                 try:
#                     if i in nums:
#                         pass

#                     else:
#                         raise ValueError("Not found")

#                 except ValueError as e:
#                     return i
                
#                 else:
#                     if(i != max_num):
#                         pass
                    
#                     else:
#                         return i+1
