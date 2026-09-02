class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []

        # almos the same as combinations

        res = []
        candidates.sort()

        def dfs(i, cur, total): 
            
            if total == target:
                res.append(cur.copy())
                return

            if i >= len(candidates) or total > target: 
                return None

            # added the next value so you have to increment the index
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])

            # dont add that value (occurences of i)
            # but what if the next value i cant just say i + 1 
            # if i choose to skip nums[i] i have to find the next non duplicate
            cur.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1 
            dfs(i + 1, cur, total)

        dfs(0, [], 0) 
        return res


            

        