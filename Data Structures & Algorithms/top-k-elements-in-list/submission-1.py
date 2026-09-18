import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for num in nums:
            count = nums_dict.get(num)
            if count == None:
                count = 0
            nums_dict[num] = count + 1

        pq = []
        for key, value in nums_dict.items():
            heapq.heappush(pq, (-value, key))

        out = []
        for num in range(k):
            val, key = heapq.heappop(pq)
            out.append(key)

        return out