class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap=[]
        origins=[]

        for i in range(0,len(points)):
            x=points[i][0]
            y=points[i][1]
            dis= (x*x) + (y*y)
            heap.append( (-dis,i) )
        heapq.heapify(heap)
        
        while len(heap) > k:
            heapq.heappop(heap)

        for item in heap:
            index=item[1]
            origins.append(points[index])
        return origins


        