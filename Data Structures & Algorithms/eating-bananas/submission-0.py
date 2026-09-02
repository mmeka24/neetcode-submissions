class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        1) you start with a minrate of 1
        2) keep dividing and stop if somethings greater 



        '''


        '''

        min_rate = 1

        while True:
            total = 0 
            for pile in piles:
                total += math.ceil(pile / min_rate)

            if total <= h:
                return min_rate

            min_rate += 1

        return min_rate

        '''

        l = 1 
        r = max(piles)
        res = r 

        while l <= r:
            mid = (l+r) // 2 

            total = 0

            for pile in piles:
                total += math.ceil(float(pile) / mid)

            if total > h: 
                l = mid + 1
            else:
                res = mid
                r = mid - 1 

        return res

        