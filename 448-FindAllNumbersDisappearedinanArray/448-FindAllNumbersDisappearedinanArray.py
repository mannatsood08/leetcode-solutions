class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        r=[]
        set_num=set(nums)
        maxx=max(nums)
        for i in range(1,len(nums)+1):
            if i not in set_num:
                r.append(i)
        return r

        