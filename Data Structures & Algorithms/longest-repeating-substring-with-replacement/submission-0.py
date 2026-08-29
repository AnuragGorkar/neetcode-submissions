class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 1
        for char_to_replace in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            i=0
            curr_count = k
            j = i
            while i<len(s):
                while j<len(s) and ((s[j] == char_to_replace) or (curr_count)):
                    if s[j] != char_to_replace:
                        curr_count -= 1
                    j += 1
                res = max(res, j-i)
                while i<len(s) and s[i] == char_to_replace:
                    i += 1
                curr_count = 1
                i += 1
        return res