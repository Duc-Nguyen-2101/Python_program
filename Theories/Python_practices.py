# https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises%20for%20Python%203.md


####################################################
# Question 1
# Level 1

# Question: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
# between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

# Hints: Consider use range(#begin, #end) method

####################################################

# for i in range(2000,3201):
#     if (i%7==0 )and (i%5!=0):
#         print(i)


####################################################
# Question 2
# Level 1

# Question: Write a program which can compute the factorial of a given numbers. 
# The results should be printed in a comma-separated sequence on a single line. 
# Suppose the following input is supplied to the program: 8 Then, the output should be: 40320

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.


# Note: this is recursive algorithm use to calculated the fractional of a number
####################################################
# def fact(x):
#     if x == 0:
#         return 1
#     return x * fact(x - 1)

# x=int(input())
# print(fact(x))


####################################################
# Question 3
# Level 1

# Question: With a given integral number n, write a program to generate a dictionary that contains (i, i*i) 
# such that is an integral number between 1 and n (both included). and then the program should print the dictionary. 
# Suppose the following input is supplied to the program: 8 Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input. Consider use dict()
####################################################

# def dicGen(x):
#     ret = {}
#     for i in range(1, x+1):
#         ret[i] = (i)*(i)

#     return ret

# x=int(input())
# print(dicGen(x))


####################################################
# Question 4
# Level 1

# Question: Write a program which accepts a sequence of comma-separated numbers from console 
# and generate a list and a tuple which contains every number. 
# Suppose the following input is supplied to the program: 34,67,55,33,12,98 
# Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input. tuple() method can convert list to tuple
####################################################
# import random

# def genList_Tup(x):
#     ret_list = []
#     ret_tuple = ()

#     for i in range(0,x):
#         num = random.randrange(0,100,1)
#         ret_list.append(num)
#         ret_tuple = tuple(ret_list)

#     print(ret_list)
#     print(tuple(ret_tuple))

# x=int(input())
# genList_Tup(x)


####################################################
# Question 5
# Level 1

# Question: Define a class which has at least two methods: 
# getString: to get a string from console input printString: to print the string in upper case. 
# Also please include simple test function to test the class methods.

# Hints: Use init method to construct some parameters

# Solution:

# class InputOutString(object):
#     def __init__(self):
#         self.s = ""

#     def getString(self):
#         self.s = input()
    
#     def printString(self):
#         print(self.s.upper())

# strObj = InputOutString()
# strObj.getString()
# strObj.printString()

####################################################

# class Solution:
#     def __init__(self) -> None:
#         self.str = ""
#         self.get_str = ""

#     def getString(self, get_str : str):
#         self.get_str = get_str
    
#     def printString(self, str : str):
#         self.str = str
#         print(self.str.upper())

# string = input()
# input = ""
# output = ""

# Test = Solution()
# Test.getString(string)
# Test.printString(string)


####################################################
# Question 6
# Level 2

# Question: Write a program that calculates and prints the value according to the given formula: 

# Q = Square root of [(2 * C * D)/H] 

# Following are the fixed values of C and H: C is 50. H is 30. 
# D is the variable whose values should be input to your program in a comma-separated sequence. 
# Example Let us assume the following comma separated input sequence is given to the program: 100,150,180 
# The output of the program should be: 18,22,24

# Hints: If the output received is in decimal form, it should be rounded off to its nearest value 
# (for example, if the output received is 26.0, it should be printed as 26) In case of input data being supplied to the question, 
# it should be assumed to be a console input.

####################################################
