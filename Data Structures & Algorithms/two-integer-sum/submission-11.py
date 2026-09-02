class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevmap = {}

        for i, num in enumerate(nums): 
            # num is value
            # i is the index

            diff = target - num

            if diff in prevmap:
                # return the indeces 
                return[prevmap[diff], i]

            prevmap[num] = i

        