class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        n = len(height)
        
        max_prefix = [0] * n
        max_prefix[0] = height[0]

        for i in range(1, n):
            max_prefix[i] = max(max_prefix[i-1], height[i])


        max_suffix = [0] * n
        max_suffix[-1] = height[-1]

        for i in range(n-2, -1, -1):
            max_suffix[i] = max(max_suffix[i+1], height[i])

        
        for i in range(n):
            water += max(0, min(max_prefix[i], max_suffix[i]) - height[i])

        return water