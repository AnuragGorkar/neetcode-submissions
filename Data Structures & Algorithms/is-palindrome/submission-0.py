class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i<j:
            while i<j and s[i] not in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                i+=1
            while j>i and s[j] not in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                j-=1
            if i<=j and s[i].lower() == s[j].lower():
                i+=1
                j-=1 
            else:
                return False  
        return True