class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left=0
        right=len(s)-1
        templ=""
        tempr=""
        while left<right:
            templ=s[left]
            tempr=s[right]
            s[left]=tempr
            s[right]=templ
            left+=1
            right-=1


        