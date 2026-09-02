class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []


        def dfs(i, cur, total):

            if target == total:
                res.append(cur.copy())
                return

            if total > target or i >= len(nums):
                return


            # chose to skip 
            dfs(i + 1, cur,total)


            #appending 
            cur.append(nums[i])
            # considering that into total
            dfs(i, cur, total + nums[i])
            cur.pop()


        dfs(0, [], 0)
        return res