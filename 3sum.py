class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)

        if(n<=2):
            return []

        result = []

        for i in range(0,n-2):
            if(nums[i]>0):
                break

            if((i>0) and (nums[i]==nums[i-1])):
                continue

            j=i+1
            k=n-1

            while(k>j):
                total = nums[i]+nums[j]+nums[k]

                if(total==0):
                    result.append([nums[i],nums[j],nums[k]])

                    while((k>j) and (nums[k]==nums[k-1])):
                        k -= 1

                    while((k>j) and (nums[j]==nums[j+1])):
                        j += 1

                    j+=1
                    k-=1
            
                elif(total<0):
                    j+=1

                else:
                    k-=1

        return result
