class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        left_bound = intervals[0][0]
        right_bound = intervals[0][1]
        
        for start, end in intervals:
            if start <= right_bound:
                right_bound = max(right_bound, end)
            else:
                res.append(([left_bound, right_bound]))
                left_bound, right_bound = start, end
        
        res.append([left_bound, right_bound])

        return res
                    

        