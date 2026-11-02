class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        if n == 0:
            return

        k %= n

        def reverse(left: int, right: int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, n - 1)  # Reverse the whole list
        reverse(0, k - 1)  # Reverse the first k elements
        reverse(k, n - 1)  # Reverse the rest
