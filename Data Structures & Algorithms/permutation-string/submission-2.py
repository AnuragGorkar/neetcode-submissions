class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict_count = defaultdict(int)
        for char in s1:
            dict_count[char] += 1
        
        i, j = 0, 0
        while i < len(s2) and j < len(s2):
            if s2[i] not in dict_count:
                i += 1
                j += 1
            else:
                while j<len(s2) and s2[j] in dict_count and dict_count[s2[j]]>0:
                    dict_count[s2[j]] -= 1
                    j += 1
                    if ((j-i) == len(s1)):
                        return True
                
                if j<len(s2) and s2[j] not in dict_count:
                    while i<j:
                        dict_count[s2[i]] += 1
                        i += 1
                
                elif j<len(s2) and dict_count[s2[j]] ==0:
                    while i<j and s2[i] != s2[j]:
                        dict_count[s2[i]] += 1
                        i += 1
                    dict_count[s2[i]] += 1
                    i += 1

        return ((j-i) == len(s1))        