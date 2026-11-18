class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums)-1
        m = l + (r - l) // 2

        if(nums[l]>nums[r]):
            while(nums[m]>=nums[m-1]):
                m = l + (r - l) // 2

                if(nums[m]<nums[r]):
                    r = m - 1

                else:
                    l = m + 1

            return nums[m]

        else:
            return nums[l]
        
