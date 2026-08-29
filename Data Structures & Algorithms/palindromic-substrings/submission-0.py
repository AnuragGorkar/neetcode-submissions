class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)): 
            # with character as center
            j, k = i, i
            while j>=0 and k<len(s) and s[j] == s[k]: 
                count += 1
                j-=1
                k+=1
            # with double character as center
            j, k = i, i+1
            while j>=0 and k<len(s) and s[j] == s[k]: 
                count += 1
                j-=1
                k+=1

        return count
        