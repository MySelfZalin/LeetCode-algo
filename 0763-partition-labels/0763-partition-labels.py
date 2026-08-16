class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        res = []
        left = 0
        curr_bound = 0

        for index, char in enumerate(s):
            last_index[char] = index
        
        for right, char in enumerate(s):
            curr_bound = max(curr_bound, last_index[char])

            if right == curr_bound:
                res.append(right - left + 1)
                left = right + 1
        return res
       





        