class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        
        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            
            if height[l] < height[r]:
                l += 1
            
            # Not necessary due to the condition below
            
            # elif height[l] > height[r]:
            #     r -= 1
            
            # Could do either l += 1 or r -= 1 when l == r. 
            else:
                r -= 1
                
        return res