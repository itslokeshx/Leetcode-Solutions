class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq={}
        for i in tasks:
            if(i not in freq):
                freq[i]=1
            else:
                freq[i]+=1
        heap=[]
        for val in freq.values():
            heap.append(-val)
        heapq.heapify(heap)
        time=0
        while heap:
            temp=[]
            for i in range(n+1):
                if(heap):
                    freq=heapq.heappop(heap)
                    freq=(freq*-1) -1
                    time+=1
                    if(freq > 0):
                        temp.append(-freq)
                else:
                    if(temp):
                        time+=1
                    else:
                        break
            for freq in temp:
                heapq.heappush(heap,freq)
        return time
            









        