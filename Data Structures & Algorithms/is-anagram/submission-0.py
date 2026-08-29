class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alpha_dict = dict()
        
        for char in s: 
            alpha_dict[char] = alpha_dict.setdefault(char, 0) + 1
        
        for char in t:
            alpha_dict[char] = alpha_dict.setdefault(char, 0) - 1
        
        for val in alpha_dict.values():
            if val != 0:
                return False

        return True