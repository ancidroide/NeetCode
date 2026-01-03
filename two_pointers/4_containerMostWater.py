class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) - 1
        max_water = 0

        while L < R:
            water = (R - L) * min(heights[L], heights[R])
            if water > max_water:
                max_water = water

            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        
        return max_water