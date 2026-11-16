# import bisect

# class Solution:
#     def searchRange(self, nums: list[int], target: int) -> list[int]:
#         left = bisect.bisect_left(nums, target)
#         right = bisect.bisect_right(nums, target) - 1

#         if left <= right and 0 <= left < len(nums) and nums[left] == target:
#             return [left, right]
#         return [-1, -1]


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def find_first(nums, target):
            l, r = 0, len(nums)
            while l < r:
                m = l + (r - l) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            return l

        first = find_first(nums, target)

        if first >= len(nums) or nums[first] != target:
            return [-1, -1]

        last = find_first(nums, target + 1) - 1

        return [first, last]
