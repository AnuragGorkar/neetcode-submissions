class Solution:
    def isHappy(self, n: int) -> bool:
        seen_set = set()
        while True:
            seen_set.add(n)
            sum = 0
            while n:
                sum += (n%10)**2
                n //= 10
            n = sum
            if n ==1:
                return True
            elif n in seen_set:
                break
        return False