class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # n log n approach 
        '''
        if not nums:
            return None
        
        nums.sort()

        longest = 1 
        streak = 1 
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            if nums[i] == nums[i-1] + 1: 
                streak += 1 
                longest = max(longest, streak)
            else:
                streak = 1
        return longest

        '''

        # best solution for this 
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                current = num 
                streak = 1

                while (current + 1) in numSet:
                    streak += 1 
                    current += 1 
                
                longest = max(longest, streak)

        return longest