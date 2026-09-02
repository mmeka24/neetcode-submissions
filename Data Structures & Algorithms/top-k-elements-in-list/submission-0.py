class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use a map to count the number of each chars
        # if that key value is greater than k add it and return 
       
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        heap = []
        for num in freq_map:
            heapq.heappush(heap, (freq_map[num], num))
            if len(heap) > k:
                heapq.heappop(heap)  # Remove least frequent

        # Step 3: Extract results from heap
        result = []
        while heap:
            result.append(heapq.heappop(heap)[1])

        return result