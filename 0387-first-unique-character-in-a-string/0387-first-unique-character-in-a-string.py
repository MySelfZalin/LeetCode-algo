class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_s = collections.Counter(s)

        for index, char in enumerate(s):
            if count_s[char] == 1:
                return index
        return -1