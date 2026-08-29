class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        val_stack = deque()

        def eval(num1, num2, op): 
            if op == '+': 
                return num1 + num2
            elif op == '-':
                return num1 - num2
            elif op == '*':
                return num1 * num2
            return int(num1 / num2)
        
        for token in tokens: 
            if token in "+-*/": 
                second_num = val_stack.pop()
                first_num = val_stack.pop()
                ans = eval(first_num, second_num, token)
                val_stack.append(ans)
            else: 
                val_stack.append(int(token))
        
        return val_stack[-1]
        