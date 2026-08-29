class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, 0
        amount = 0
        while l<len(height) and r<len(height): 
            fill_till_height = height[l]
            r+=1
            while r<len(height) and height[r]<fill_till_height: 
                r+=1
            if r<len(height):
                while l<r: 
                    amount += fill_till_height-height[l]
                    l+=1
            else: 
                break

        lim = l
        l, r = len(height)-1, len(height)-1
        while l>=lim and r>=lim: 
            fill_till_height = height[r]
            l-=1
            while l>=lim and height[l]<fill_till_height: 
                l-=1
            if l>=lim:
                while l<r: 
                    amount += fill_till_height-height[r]
                    r-=1
        
        return amount

        