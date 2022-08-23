# Time Complexity : O(2^m*n)
# Space Complexity : O(n^2) 
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        if (candidates == None):
            return self.result
        self.helper(candidates, 0, target, [])
        return self.result
    
    def helper(self, candidates, pivot, amount, path): 
        #base
        if(amount < 0):
            return 
        if(amount == 0):
            self.result.append(path)
            return
        #logic
        for i in range(pivot, len(candidates)):
            temp = path[:]
            temp.append(candidates[i])
            self.helper(candidates, i, amount - candidates[i], temp)
