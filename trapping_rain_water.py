class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height)-1
        max_left, max_right = height[0], height[-1]
        water = 0

        while(left<right):
            if(height[left]<height[right]):
                left += 1
                max_left = max(max_left,height[left])
                water += max_left - height[left]

            else:
                right -= 1
                max_right = max(max_right,height[right])
                water += max_right - height[right]

        return water
