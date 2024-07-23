class Solution:
    def romanToInt(self, s: str) -> int:
        Data_sym = ["I", "V", "X", "L", "C", "D", "M"]
        Data_val = [1, 5, 10, 50, 100, 500, 1000]
        ret = 0

        for i in range(len(Data_sym)):
            for j in range(len(s)):
                if s[j] == Data_sym[i]:
                    ret = ret + Data_val[i]
                
        return ret

Test = Solution()
print(Test.romanToInt("MMXXVIII"))

        