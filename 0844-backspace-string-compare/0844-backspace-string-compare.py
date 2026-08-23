class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        p1 = len(s)
        p2 = len(t)

        def find_next_position(s: str, index: int) -> int:
            counter_hashtags = 0
            while index >= 0 and (counter_hashtags > 0 or s[index] == '#'):
                if s[index] == '#':
                    counter_hashtags += 1
                    index -= 1
                    continue
                counter_hashtags -= 1
                index -= 1
            return index

        while p1 > 0 and p2 > 0:
            p1 = find_next_position(s, p1 - 1)
            p2 = find_next_position(t, p2 - 1)

            if p1 >= 0 and p2 >= 0 and s[p1] != t[p2]:
                return False

        return find_next_position(s, p1 - 1) == find_next_position(t, p2 - 1)
        