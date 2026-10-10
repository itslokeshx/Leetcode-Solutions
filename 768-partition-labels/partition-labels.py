class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        freq={}
        start=0
        end=0
        result=[]
        for i in range(len(s)):
            if( s[i] not in freq):
                freq[s[i]]=i
            else:
                freq[s[i]]=i
        for i in range(len(s)):
            end=max(end,freq[s[i]])
            if(i == end):
                result.append(i-start+1)
                start=i+1
        return result

        
        