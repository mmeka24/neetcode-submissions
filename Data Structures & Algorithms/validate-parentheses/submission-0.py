class Solution:
    def isValid(self, s: str) -> bool:
        # brute force is just doing white space 

        '''
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        
        return s == ''

        '''

        # using a stack

        stack = []

        dicti = {")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c in dicti:
                if not stack or stack.pop() != dicti[c]:
                    return False
            else:
                stack.append(c)
        
        
        return len(stack) == 0
            