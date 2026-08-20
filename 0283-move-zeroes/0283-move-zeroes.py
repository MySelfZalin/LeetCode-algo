class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write = 0
        for read, num in enumerate(nums):
            if num != 0:
                nums[write], nums[read] = nums[read], nums[write]
                write += 1
                
        