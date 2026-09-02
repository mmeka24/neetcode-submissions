class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        prevmap = {}

        for i, num in enumerate(nums):
            # gives index i and num
            diff = target - num
            if diff in prevmap:
                return [prevmap[diff], i]
            prevmap[num] = i


        


        
        