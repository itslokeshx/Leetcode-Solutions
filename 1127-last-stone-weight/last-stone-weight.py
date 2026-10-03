class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap=[]
        for n in stones:
            heap.append(n*-1)
        heapq.heapify(heap)
        while len(heap) >= 2:
            if(heap[0]*-1 == heap[1]*-1):
                heapq.heappop(heap)
                heapq.heappop(heap)
            elif(heap[0]*-1 > heap[1] *-1):
                max=heapq.heappop(heap)
                min=heapq.heappop(heap)
                final=(max*-1) - (min*-1)
                heapq.heappush(heap,final * -1)
        if(len(heap)==0):
            return 0
        return heap[0]*-1

        