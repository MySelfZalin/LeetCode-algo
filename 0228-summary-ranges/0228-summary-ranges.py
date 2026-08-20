class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        res = []
        val1 = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                continue

            if nums[i-1] == val1:
                res.append(f"{val1}")
            else:
                res.append(f"{val1}->{nums[i-1]}")
            val1 = nums[i]    

        if val1 == nums[-1]:
            res.append(f"{val1}")
        else:
            res.append(f"{val1}->{nums[-1]}")
        
        return res



        