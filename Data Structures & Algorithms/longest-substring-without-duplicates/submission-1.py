class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s):
            return 0

        i, j = 0, 1
        dict_count = dict()
        dict_count[s[i]] = dict_count.setdefault(s[i], 0) + 1

        max_len = 1
        
        while j<len(s):
            if s[j] in dict_count and dict_count[s[j]] > 0:
                max_len = max(j-i, max_len)
                while s[i] != s[j]:
                    dict_count[s[i]] -= 1    
                    i += 1
                i += 1
            else:
                dict_count[s[j]] = dict_count.setdefault(s[j], 0) + 1
            j += 1
        
        return max(max_len, j-i)