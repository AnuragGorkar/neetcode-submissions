class Solution:
    def isValid(self, s: str) -> bool:
        par_stack = deque()

        for par in s: 
            if par in '([{':
                par_stack.append(par)
            else: 
                if not len(par_stack) or (par == ']' and par_stack[-1] != '[') or (par == ')' and par_stack[-1] != '(') or (par == '}' and par_stack[-1] != '{'): 
                    return False
                par_stack.pop()
            

        return len(par_stack)==0
        