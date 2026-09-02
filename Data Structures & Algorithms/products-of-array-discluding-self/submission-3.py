class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #brute force  O(n^2)

        leng = len(nums)
        res = nums.copy()
        i = 0

        for i in range(leng):
            prod = 1
            for j in range(leng):
                if i == j:
                    continue
                prod *= nums[j]
            res[i] = prod
        return res








        # more optimal O(n)