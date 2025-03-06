class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(pat: list[int], s:int):
            if len(pat) == k:
                res.append(pat[:])
                return 
            for i in range(s, n+1):
                pat.append(i)
                backtrack(pat, i+1)
                pat.pop()
        backtrack([], 1)
        return res
        