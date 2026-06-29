class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        arr = [0] * len(nums)
        flag = 0
        for i in nums:
            if i != 0:
                prod *= i
            else:
                flag +=1 
        if flag > 1:
            return arr
        for i in range(len(nums)):
            if flag == 1:
                if nums[i] == 0:
                    arr[i] = prod
                else:
                    arr[i] = 0
            else:
                arr[i] = prod // nums[i]
        return arr