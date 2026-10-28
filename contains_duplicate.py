class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        list_nums=nums
        set_nums=set(nums)
        if ((len(list_nums))!=(len(set_nums))):
            return True
        else:
            return False
