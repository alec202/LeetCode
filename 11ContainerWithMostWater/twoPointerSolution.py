from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0
        while l < r:
            width = min(height[l], height[r])
            length = (r) - (l)
            area = (width) * length
            if area > max_area:
                max_area = area
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area


"""
height = [1,8,6,2,5,4,8,3,7]
l = 1
r = 7
width = 7
length = 7
area = 49
max_area = 49

"""

