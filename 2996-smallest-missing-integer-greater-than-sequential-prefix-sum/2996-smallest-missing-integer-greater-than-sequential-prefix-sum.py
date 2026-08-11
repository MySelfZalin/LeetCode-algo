class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        pref_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                break
            pref_sum += nums[i]

        nums_set = set(nums)

        while pref_sum in nums_set:
            pref_sum += 1

        return pref_sum    



        