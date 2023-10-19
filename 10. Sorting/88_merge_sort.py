class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        a = m-1
        b = n-1
        write_index = m + n -1

        while b >= 0:
            if a >= 0 and nums1[a] > nums2[b]:
                nums1[write_index] = nums1[a]
                a -=1
            else:
                nums1[write_index] = nums1[b]
                b -=1
            write_index -=1

nums1 = [1,2,3]
nums2 = [2,5,6]
result = Solution()
result.merge()