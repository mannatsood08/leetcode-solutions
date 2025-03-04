class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res=[]
        strset=set(nums)
        for i in range(1,len(nums)+1):
            if i not in strset:
                res.append(i)
        return res

        