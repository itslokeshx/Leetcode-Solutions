class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        seen=set()
        value={}
        count=0
        replace_needed=0
        most_freq=0
        for right in range(0,len(s)):
            if(s[right] not in seen):
                seen.add(s[right])
                value[s[right]]=1
            else:
                value[s[right]]+=1
            most_freq=max(value.values())
            replace_needed=(right-left+1)-most_freq
            while(replace_needed>k):
                value[s[left]]-=1
                left+=1
                most_freq=max(value.values())
                replace_needed=(right-left+1)-most_freq
            count=max(count,right-left+1)
        return count
        