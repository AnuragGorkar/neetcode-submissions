class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(open_count, close_count, curr_string):
            if close_count == n: 
                res.append(curr_string[:])
            else: 
                if open_count<n:
                    curr_string += '('
                    dfs(open_count+1, close_count, curr_string)
                    curr_string = curr_string[:-1]

                if close_count<open_count:
                    curr_string += ')'
                    dfs(open_count, close_count+1, curr_string)
                    curr_string = curr_string[:-1]

        dfs(0, 0, "")
        return res
        