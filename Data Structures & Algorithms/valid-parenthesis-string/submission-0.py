from functools import lru_cache

class Solution:       
    def checkValidString(self, s: str) -> bool:

        @lru_cache(None)
        def dfs(s, index, open_count, close_count):
            if index == len(s):
                return open_count == close_count
            else:
                if s[index] != '*':
                    if s[index] == '(':
                        open_count+=1
                    else:
                        close_count += 1
                    if close_count>open_count:
                        return False
                    return dfs(s, index+1, open_count, close_count)
                else:
                    empty, opened, closed = False, False, False
                    if open_count>close_count:
                        closed = dfs(s, index+1, open_count, close_count+1)
                    opened = dfs(s, index+1, open_count+1, close_count)
                    empty = dfs(s, index+1, open_count, close_count)
                    return (empty or opened or closed) 
        
        return dfs(s, 0, 0, 0)