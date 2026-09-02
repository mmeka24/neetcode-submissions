class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]


        for i in range(1, len(intervals)):

            # if the start of the next is less than the 
            if intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                # just append normally
                res.append(intervals[i])

        return res