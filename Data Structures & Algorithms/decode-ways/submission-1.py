class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s)==0 or (len(s)==1 and s[0] != '0'): 
            return 1
        elif s[0] == '0': 
            return 0
        else:
            take_1 = self.numDecodings(s[1:])
            take_2 = 0 
            if (s[0] == '1') or (s[0] == '2' and s[1] in ['0', '1', '2', '3', '4', '5', '6']): 
                take_2 = self.numDecodings(s[2:])
            return take_1 + take_2
        