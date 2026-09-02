class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        2 pointer question going to have a fast and slow pointer
        '''

        # option 1: 2 for loops obv
        # option 2: binary search

        for i in range(len(numbers)):
            l = 0
            r = len(numbers) - 1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r - l)//2
                if numbers[mid] == tmp:
                    return [i + 1, mid + 1]
                elif numbers[mid] < tmp:
                    l = mid + 1
                else:
                    r = mid - 1
        return []
    '''
        while l < r: 
            current_sum = numbers[l] + numbers[r]

            if current_sum < target:
                l += 1

            if current_sum > target:
                r -= 1

            if current_sum == target:
                # +1 because the problem expects 1-indexed results
                return [l + 1, r + 1]
'''

       

        