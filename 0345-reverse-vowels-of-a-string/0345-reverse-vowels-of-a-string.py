class Solution:
    def reverseVowels(self, s: str) -> str:
        list_chars = list(s)
        chars = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        left = 0
        right = len(list_chars) - 1
        while left < right:
            if list_chars[left] not in chars:
                left += 1
                continue
            if list_chars[right] not in chars:
                right -= 1
                continue
            
            list_chars[left], list_chars[right] = list_chars[right], list_chars[left]
            left += 1
            right -= 1
        return "".join(list_chars)
        