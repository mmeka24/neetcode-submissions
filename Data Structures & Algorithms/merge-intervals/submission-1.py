class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for i in range(1, len(intervals)): 
            # if the first value of res
            if res[-1][1] >= intervals[i][0]:
                # merge 
                res[-1] = [min(res[-1][0], intervals[i][0]), 
                        max(res[-1][1], intervals[i][1])]
                
                #intervals[i] = merged
            else:
                res.append(intervals[i])

        return res

            
            