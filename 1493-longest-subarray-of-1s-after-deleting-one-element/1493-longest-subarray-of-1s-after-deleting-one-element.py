class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        seen_zero = 0
        left = 0
        max_res = 0

        for right, num in enumerate(nums):
            if num == 0:
                seen_zero += 1
                while seen_zero > 1:
                    if nums[left] == 0:
                        seen_zero -= 1
                    left += 1    

            max_res = max(max_res, right - left)   

        return max_res