class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = len(str(x))
        ret = False
        for i in range(n):
            if str(x)[i] != str(x)[n-1-i]:
                ret = False
                break
            else:
                ret = True
        return ret
            
        

Test = Solution()

# 12321 - PASSED
print("TEST 1 - ")
print(Test.isPalindrome(12321))

# -12321 - PASSED
print("TEST 2 - ")
print(Test.isPalindrome(-12321))

# 12322221 - PASSED
print("TEST 3 - ")
print(Test.isPalindrome(12322221))

# 11111333111 - PASSED
print("TEST 4 - ")
print(Test.isPalindrome(11111333111))