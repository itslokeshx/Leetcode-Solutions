class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        ranges=[]
        path=""
        start=0
        end=0
        if(len(nums) == 0):
            return []
        for i in range(1,len(nums)):
            if( nums[i] == nums[i-1] +1 ): 
                end+=1
                continue
            
            if(start!=end):
                path+=str(nums[start])+ "->"+str(nums[end])
                ranges.append(path)
                path=""
                start=end+1
                end+=1
            else:
                path+=str(nums[end])
                ranges.append(path)
                path=""
                start=end+1
                end+=1

        if(start!=end):
            path+=str(nums[start])+ "->"+str(nums[end])
            ranges.append(path)
            path=""
            start=end+1
            end+=1
        else:
            path+=str(nums[end])
            ranges.append(path)
            path=""
            start=end+1
            end+=1

        return ranges






        