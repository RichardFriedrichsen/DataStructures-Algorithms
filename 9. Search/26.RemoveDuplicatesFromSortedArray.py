# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. 
# Then return the number of unique elements in nums.
# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        index = 0

        #return unique elements
        # return the array num with

        for no in range(0,len(nums)):
            # either Unique is equal to next
                if no+1 < len(nums) and nums[no] == nums[no+1]:
                   
                   print("not equal")
                
            # or Unique element is not equal to next
                elif no+1 < len(nums) and nums[no] != nums[no+1]:
                    print("equal")
                    index += 1
                    nums[index] = nums[no+1]
                print(nums)
        
        return index + 1
nums = [0,0,1,1,1,2,2,3,3,4]
# nums = [1,1,2]
solution = Solution()
solution.removeDuplicates(nums)


