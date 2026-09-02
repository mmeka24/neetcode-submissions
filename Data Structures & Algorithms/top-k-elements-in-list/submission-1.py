class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # heap problem 

        heap = []
        # max heap of how frequent a value is
        # heap will store num and frequency 
        frequency = {}
        for num in nums:
            frequency[num] = 1 + frequency.get(num, 0)
            # 1, 2, 2, 3, 3, 3 -> 1:1, 2:2, 3:3 

        for num in frequency.keys():
            heapq.heappush(heap, (frequency[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res