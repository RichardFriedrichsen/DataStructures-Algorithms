class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        int_a = int(a,2)
        int_b = int(b,2)

        sum_ints = int_a + int_b
        bin_sum = bin(sum_ints)
        binsum = bin_sum[2:]
        return binsum

solution = Solution()

solution.addBinary("11","1")