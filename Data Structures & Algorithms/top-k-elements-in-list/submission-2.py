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

        # gpo through the keys 
        for num in frequency.keys():
            # push to heap the frequency of that num along with num
            # 2: 1, 3:4 6:1 
            # stored in min heap by default so in above order
            heapq.heappush(heap, (frequency[num], num))

            # maintain only k items so pop from the top 
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            # pop from the top 
            res.append(heapq.heappop(heap)[1])

        return res