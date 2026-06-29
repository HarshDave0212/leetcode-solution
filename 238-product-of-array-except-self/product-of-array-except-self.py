class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        pref = 1
        for i in range(len(nums)):
            ans[i] *= pref
            pref *= nums[i]
        suff = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= suff
            suff *= nums[i]
        return ans