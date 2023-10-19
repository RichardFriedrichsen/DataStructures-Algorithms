class Solution:
    def removeElement(self, nums, val) -> int:
        
        pointer = 0

        for x in nums:
            if x != val:
                nums[pointer] = x
                pointer += 1
        return pointer
                



nums = [5,2,5,8,4,5,6,3,2,5,8,4,1,2,5,4,2]
val = 5
result = Solution()
result.removeElement(nums,val)