class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        net=[0]*len(gas)
        start=0
        tank=0
        for i in range(len(cost)):
            net[i]=gas[i]-cost[i]
        if(sum(net) <0):
            return -1
        for i in range(len(net)):
            tank+=net[i]
            if(tank < 0):
                tank=0
                start=i+1
        return start





        