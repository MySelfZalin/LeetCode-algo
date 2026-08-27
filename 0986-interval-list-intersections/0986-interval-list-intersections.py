class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        index_first = index_second = 0
        res = []
        
        while index_first < len(firstList) and index_second < len(secondList):
            start1, end1 = firstList[index_first]
            start2, end2 = secondList[index_second]
            
            if max(start1, start2) <= min(end1, end2):
                res.append([max(start1, start2), min(end1, end2)])
            
            if end1 < end2:
                index_first += 1
            else:
                index_second += 1
        
        return res