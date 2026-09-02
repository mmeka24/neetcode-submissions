class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total): 
            
            if total == target:
                res.append(cur.copy())
                return

            if i >= len(nums) or total > target: 
                return None

            # added that value 
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            # dont add that value (occurences of i)
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0) 
        return res


            