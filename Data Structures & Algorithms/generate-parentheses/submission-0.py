class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        stack = []
        res = []

        def backtrack(open_num, close_num):
            if open_num == close_num == n:
                res.append("".join(stack))

            if open_num > close_num:
                stack.append(")")
                backtrack(open_num, close_num + 1 )
                stack.pop()


            if open_num < n:
                stack.append("(")
                backtrack(open_num + 1, close_num)
                stack.pop()
        
        backtrack(0,0)
        return res