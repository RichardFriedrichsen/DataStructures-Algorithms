class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        arr = []
        arr = s.rsplit()
        length = len(arr)
        length_last_word = len(arr[length-1])
        return length_last_word
        
s = "   fly me   to   the moon  "
result = Solution()
result.lengthOfLastWord(s)