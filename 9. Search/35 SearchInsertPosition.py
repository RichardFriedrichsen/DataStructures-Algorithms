class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi)//2
            if nums[mid] < target:
                lo = mid +1
            else:
                hi = mid
        return lo

       




nums,target = [1,3,5,6], 5
# Output: 2
# Example 2:

# nums,target = [1,3,5,6], 2
# Output: 1
# Example 3:

# nums,target = [1,3,5,6], 7
# Output: 4

solution = Solution()
solution.searchInsert(nums, target)