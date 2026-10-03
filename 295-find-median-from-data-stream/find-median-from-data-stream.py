class MedianFinder:
    def __init__(self):
        self.low=[]
        self.high=[]
        
    def addNum(self, num: int) -> None:

        heapq.heappush(self.low,-num)

        if( self.high and self.high[0] < -self.low[0] ):
            x=heapq.heappop(self.low)
            heapq.heappush(self.high,-x)
        
        if( len(self.low) > len(self.high) + 1 ):
            x=heapq.heappop(self.low)
            heapq.heappush(self.high,-x)

        elif len(self.high) > len(self.low):
            x = heapq.heappop(self.high)
            heapq.heappush(self.low, -x)

    def findMedian(self) -> float:

        if(len(self.low) == len(self.high)):
            return ((self.low[0] * -1) + self.high[0]) /2
        else:
            return -self.low[0]

            

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()