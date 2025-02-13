from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        initial_length = min(height[0], height[1])
        initial_width = 1
        max_area = initial_length * initial_width
        for h1_i in range(0, len(height)):
            for h2_i in range(h1_i + 1, len(height)):
                height_here = min(height[h1_i], height[h2_i])
                width_here = (h2_i) - (h1_i)
                area_here = height_here * width_here
                if area_here > max_area:
                    max_area = area_here
        return max_area


"""
height = [1,8,6,2,5,4,8,3,7]
inital_length = 1
initial_width = 1
max_area = 2
h1_i = 0
h2_i = 2
height_here = 1
width_here = 2
area_here = 2

"""

