class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        perm = []

        def dfs(): 

            # base condition 
            if len(nums) == len(perm):
                res.append(perm.copy()) 
                return 

            
            for num in nums:
                if num not in perm: 
                    perm.append(num)
                    dfs()
                    perm.pop()

        dfs()

        return res



