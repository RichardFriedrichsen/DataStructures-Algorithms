class Solution(object):
    

    my_basic_Dict = {
            'I':1,
            'IV':4,
            'V':5,
            'IX':9,
            'X':10,
            'XL':40,
            'L':50,
            'XC':90,
            'C':100,
            'CD':400,
            'D':500,
            'CM':900,
            'M':1000,
            }

            



    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        running_total = 0

        # Loop through every charackter in S and see if 
        i = 0
        while i+1 < len(s):
            current_check = s[i] + s[i+1]

            try: 
                running_total += Solution.my_basic_Dict[current_check]
                print("Try")
                print(current_check)
                print(running_total)
                print(i)
                i +=2
            except KeyError:
                running_total += Solution.my_basic_Dict[s[i]]
                print("Except")
                print(current_check)
                print(running_total)
                print(i)
                i +=1       
        
        if i <= len(s)-1:
            print(i)
            print(len(s))
            running_total += Solution.my_basic_Dict[s[i]]
            print(running_total)
        

result = Solution()
result.romanToInt("LVIII")
# 1994
# IV = 4
# XC = 90

