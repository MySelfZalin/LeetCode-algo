class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min(len(word) for word in strs)

        pref = []
        for i in range(min_len):
            curr_char = strs[0][i]

            for word in strs:
                if word[i] != curr_char:
                    return "".join(pref)
            pref.append(curr_char)

        return "".join(pref)
        