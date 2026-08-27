class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        counts = Counter(dict(nums1)) + Counter(dict(nums2))
        
        return sorted([id_, val] for id_, val in counts.items())