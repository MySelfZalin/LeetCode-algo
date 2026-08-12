class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        left = 0
        res = []

        for right, num in enumerate(nums):
            if right and num != nums[right - 1] + 1:
                res.append(f"{nums[left]}->{nums[right-1]}" if right - left > 1 else f"{nums[left]}")
                left = right

        res.append(f"{nums[left]}->{nums[-1]}" if len(nums) - left > 1 else f"{nums[left]}")
               

        return res         


