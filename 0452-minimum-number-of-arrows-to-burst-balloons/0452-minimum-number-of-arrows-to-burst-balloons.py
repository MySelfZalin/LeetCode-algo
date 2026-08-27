class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
    
        res = 0
        right_bound = float('-inf')
        
        for left, right in points:
            if left > right_bound:
                res += 1
                right_bound = right
            else:
                right_bound = min(right_bound, right)
        return res
        