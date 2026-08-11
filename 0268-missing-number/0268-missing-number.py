class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        expended_sum = (n*(n+1)) // 2
        curr_sum = sum(nums)
        return expended_sum - curr_sum
        
        