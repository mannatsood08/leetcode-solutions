class Solution:
    def minCut(self, s: str) -> int:
        dp={}
        def palindromePartitioning(w,ans):
            if w in dp:return dp[w]
            
            if w==w[::-1]:
                return 0
            
            
            for i in range(len(w)):
                curr=w[:i+1]
                
                if curr==curr[::-1]:
                    ans=min(ans,1+palindromePartitioning(w[i+1:],ans))
                    dp[w]=ans
                
                
            
            

            return ans
        

        return palindromePartitioning(s,len(s)-1)