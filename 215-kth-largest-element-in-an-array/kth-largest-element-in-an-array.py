class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap=nums
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)
        return heap[0]

        