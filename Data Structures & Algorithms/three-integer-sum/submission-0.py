class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        nums.sort()
        result = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # skip duplicate i
                continue
            
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                
                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:  # skip duplicate l
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:  # skip duplicate r
                        r -= 1
                    l += 1
                    r -= 1

        return result