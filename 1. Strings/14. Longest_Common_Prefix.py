class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        res = ""
        v = sorted(strs)
        print(v)
        for i in range(min(len(v[0]),len(v[-1]))):
            if v[0][i] != v[-1][i]:
                return res
            res += v[0][i]
        return res 

        
       

            
        
        


                

        

strs = ["dog","racecar","car"]
# strs = ["flower","flow","flight"]
# strs = ["ab","a"]

solution = Solution()
solution.longestCommonPrefix(strs)
