class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        maxele=-1
        gedict={}
        for i in range(0,len(nums2)):
            for j in range(i+1,len(nums2)):
                if(nums2[i] < nums2[j]):
                    gedict[nums2[i]]=nums2[j]
                    break

        op=[]
        for i in range(len(nums1)):
            if(nums1[i] in gedict):
                if(nums1[i] == nums2[-1]):
                    op.append(-1)
                else:
                    op.append(gedict[nums1[i]])
            else:
                op.append(-1)
        return op

        