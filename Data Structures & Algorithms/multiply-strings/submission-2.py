class Solution:

    def multiply(self, num1: str, num2: str) -> str:
        def str_to_int(s):
            char_to_int = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}
            n = 0
            for dig in s:
                n = n*10 + char_to_int[dig]
            return n

        def int_to_str(n):
            int_to_char = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9"}
            s = ""
            while n:
                s += int_to_char[n%10]
                n //= 10
            if s == "":
                return "0"
            return s[::-1]

        num1 = str_to_int(num1)
        num2 = str_to_int(num2)
        return int_to_str(num1*num2)