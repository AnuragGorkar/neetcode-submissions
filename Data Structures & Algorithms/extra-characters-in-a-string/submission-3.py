from functools import lru_cache
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        @lru_cache(None)
        def recurBreak(index):
            if index == len(s):
                return 0
            
            dropped = 1 + recurBreak(index+1)
            for i in range(index, len(s)):
                if s[index: i+1] in dictionary:
                    dropped = min(dropped, recurBreak(i+1))

            return dropped 
        return recurBreak(0)    