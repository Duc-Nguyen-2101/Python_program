class Solution:
    def romanToInt(self, s: str) -> int:
        Data_sym = ["I", "V", "X", "L", "C", "D", "M"]
        Data_val = [1, 5, 10, 50, 100, 500, 1000]
        ret = 0

        for i in range(len(Data_sym)):
            for j in range(len(s)):
                if s[j] == Data_sym[i]:
                    ret = ret + Data_val[i]
                    if i % 2 == 0:
                        if j < len(s) - 1:
                            if s[j] == "I" and s[j+1] == "V":
                                ret = ret - 2
                            elif s[j] == "I" and s[j+1] == "X":
                                ret = ret - 2
                            elif s[j] == "X" and s[j+1] == "L":
                                ret = ret - 20
                            elif s[j] == "X" and s[j+1] == "C":
                                ret = ret - 20
                            elif s[j] == "C" and s[j+1] == "D":
                                ret = ret - 200
                            elif s[j] == "C" and s[j+1] == "M":
                                ret = ret - 200  
        return ret


Test = Solution()
print(Test.romanToInt("MCMXCV"))

        