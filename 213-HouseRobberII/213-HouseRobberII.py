def solve(arr):
    
    n=len(arr)
    prev=arr[0]
    prev2=0
    for i in range(1,n):
        p=arr[i]
        if i>1:
            p+=prev2
        np=prev
        curr=max(p,np)
        prev2=prev
        prev=curr
    return prev
class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        arr1=[]
        arr2=[]
        for i in range(n):
            if i!=0:
                arr1.append(nums[i])
            if i!=n-1:
                arr2.append(nums[i])
        k=solve(arr1)
        l=solve(arr2)
        return max(k,l)
        