class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Goal is ans[i] = product of all left element i x product of all right element
        n = len(nums)
        ans = []
        
        prefix = 1
        
        for i in range(n):
            ans.append(prefix)
            prefix *= nums[i]
        
        suffix = 1
        
        for i in range(n-1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]
                 
        return ans





        
        
                

