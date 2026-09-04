class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        if n == 0: return 0

        leftMax = [0]*n
        righMax = [0]*n

        leftMax[0] = height[0]

        for i in range(1,n):
            leftMax[i] = max(leftMax[i-1],height[i])


        righMax[n-1] = height[n-1]
        for j in range(n-2,-1,-1):
            righMax[j] = max(righMax[j+1], height[j])

        
        res =0
        for i in range(n):
            res += min(leftMax[i], righMax[i]) - height[i]

        return res