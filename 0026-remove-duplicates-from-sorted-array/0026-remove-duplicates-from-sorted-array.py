class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 0
        last_num = None
        for num in nums:
            if num != last_num:
                last_num = num
                nums[write] = num
                write += 1
        return write        