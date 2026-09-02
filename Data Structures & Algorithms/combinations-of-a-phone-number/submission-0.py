class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        create a map of all 
        '''
        if not digits:
            return []

        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i, curStr):
            if len(digits) == i: 
                res.append("".join(curStr.copy()))
                return
            for ch in digitToChar[digits[i]]:
                curStr.append(ch)
                dfs(i + 1, curStr)
                curStr.pop()


        dfs(0, [])
        return res 