class MedianFinder:

    def __init__(self):
        # small is a max heap 
        self.small = []
        # large is a min heap 
        self.large = []
        

    def addNum(self, num: int) -> None:
        # put it in max heap 
        heapq.heappush(self.small, -num)
        
        # make sure that elements in small <= large heap
        if (self.small and self.large and (-self.small[0] > self.large[0])):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # uneven size

        if len(self.small) > len(self.large) + 1:
            # move to the lare
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1: 
            # move to the small because large has more vals
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            # odd number of elements
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]

        return (-1 * self.small[0] + self.large[0]) / 2
        

        
        