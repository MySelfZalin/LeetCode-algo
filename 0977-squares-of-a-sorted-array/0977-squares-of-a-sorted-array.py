class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        left, right = 0, len(nums) - 1
        pointer = len(nums) - 1

        while left <= right:
            if abs(nums[right]) > abs(nums[left]):
                res[pointer] = nums[right]**2
                right -= 1
            else:
                res[pointer] = nums[left]**2
                left += 1
            pointer -= 1
        
        return res
        