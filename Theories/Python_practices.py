# https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises%20for%20Python%203.md


####################################################
# Question 1
# Level 1

# Question: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
# between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

# Hints: Consider use range(#begin, #end) method

# Solution:

# l=[]
# for i in range(2000, 3201):
#     if (i%7==0) and (i%5!=0):
#         l.append(str(i))

# print(','.join(l))
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
# Solution:

# def fact(x):
#     if x == 0:
#         return 1
#     return x * fact(x - 1)

# x=int(input())
# print(fact(x))
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
# Solution:

# n=int(input())
# d=dict()
# for i in range(1,n+1):
#     d[i]=i*i

# print(d)
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

# Solution:

# values=input()
# l=values.split(",")
# t=tuple(l)
# print(l)
# print(t)
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
# import math

# def squareRoot(D : int):
#     Q : int = 0
#     C : int = 50
#     H : int = 30
#     Q = int(round((math.sqrt((2*C*D)/H)) , 0))
#     return Q 

# print(squareRoot(100), squareRoot(150), squareRoot(180))

####################################################
# Question 7
# Level 2

# Question: Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
# The element value in the i-th row and j-th column of the array should be i*j. Note: i=0,1.., X-1; j=0,1,¡­Y-1. 
# Example Suppose the following inputs are given to the program: 3,5 
# Then, the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

# Hints: Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.

# Solution:

# input_str = input()
# dimensions=[int(x) for x in input_str.split(',')]
# rowNum=dimensions[0]
# colNum=dimensions[1]
# multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

# for row in range(rowNum):
#     for col in range(colNum):
#         multilist[row][col]= row*col

# print(multilist)
####################################################

# def arrayGen(X:int, Y:int):
#     ret = []
#     for i in range(0,X):
#         ret.append([])
#         for j in range(0,Y):
#             ret[i].append(i*j)
#     return ret

# print(arrayGen(3,5))


####################################################
# Question 8
# Level 2

# Question: Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence 
# after sorting them alphabetically. Suppose the following input is supplied to the program: without,hello,bag,world 
# Then, the output should be: bag,hello,without,world

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

# Solution:

# items=[x for x in input().split(',')]
# items.sort()
# print(','.join(items))
####################################################

# input_str = input()
# output_str=[str(x) for x in input_str.split(',')]

# str_sort = sorted(output_str)
# print(str_sort)

####################################################
# Question 9
# Level 2

# Question£º Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized. 
# Suppose the following input is supplied to the program: Hello world Practice makes perfect 
# Then, the output should be: HELLO WORLD PRACTICE MAKES PERFECT

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

# Solution:

# lines = []
# while True:
#     s = input()
#     if s:
#         lines.append(s.upper())
#     else:
#         break;

# for sentence in lines:
#     print(sentence)
####################################################

# input_str = input()
# print(input_str.upper())

####################################################
# Question 10
# Level 2

# Question: Write a program that accepts a sequence of whitespace separated words as input 
# and prints the words after removing all duplicate words and sorting them alphanumerically. 
# Suppose the following input is supplied to the program: hello world and practice makes perfect and hello world again 
# Then, the output should be: again and hello makes perfect practice world

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input. 
# We use set container to remove duplicated data automatically and then use sorted() to sort the data.

# Solution:
# s = input()
# words = [word for word in s.split(" ")]
# print(" ".join(sorted(list(set(words)))))
####################################################

# input_str = input()
# output_str = str(input_str).split(' ')
# ret = []

# for i in range(0, len(output_str)-1):
#     if output_str[i] not in ret:
#         ret.append(output_str[i])


# print(' '.join(ret))

####################################################
# Question 11
# Level 2

# Question: Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and 
# then check whether they are divisible by 5 or not. 
# The numbers that are divisible by 5 are to be printed in a comma separated sequence. 
# Example: 0100,0011,1010,1001 Then the output should be: 1010 
# Notes: Assume the data is input by console.

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

# Solution:
# value = []
# items=[x for x in input().split(',')]
# for p in items:
#     intp = int(p, 2)
#     if not intp%5:
#         value.append(p)

# print(','.join(value))
####################################################

# num = input()
# num_bit = [str(x) for x in num.split(',')]
# ret = []

# for x in num_bit:
#     value = int(x, 2)
#     if not value%5:
#         ret.append(x)

# print(','.join(ret))


####################################################
# Question 12
# Level 2

# Question: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number. 
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

# Solution:
# values = []
# for i in range(1000, 3001):
#     s = str(i)
#     if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
#         values.append(s)
# print(",".join(values))

####################################################

# ret = []
# for val in range(1000,3001):
#     s = str(val)
#     if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
#         ret.append(str(val))

# print(",".join(ret))


####################################################
# Question 13
# Level 2

# Question: Write a program that accepts a sentence and calculate the number of letters and digits. 
# Suppose the following input is supplied to the program: hello world! 123 
# Then, the output should be: LETTERS 10 DIGITS 3

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

# Solution:
# s = input()
# d={"DIGITS":0, "LETTERS":0}
# for c in s:
#     if c.isdigit():
#         d["DIGITS"]+=1
#     elif c.isalpha():
#         d["LETTERS"]+=1
#     else:
#         pass
# print("LETTERS", d["LETTERS"])
# print("DIGITS", d["DIGITS"])

####################################################

# input_str = input()
# s = [str(x) for x in input_str.split(' ')]

# character_count = 0
# digit_cout = 0
# specical_count = 0

# for characters in s:
#     for x in range(0, len(characters)):
#         if characters[x].isalpha():
#             character_count += 1
#         elif characters[x].isdigit():
#             digit_cout += 1
#         else:
#             specical_count +=1
                   
# print("LETTERS " + str(character_count))
# print("DIGITS " + str(digit_cout))
# print("SPECIAL CHARACTER " + str(specical_count))


####################################################
# Question 14
# Level 2

# Question: Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters. 
# Suppose the following input is supplied to the program: Hello world! 
# Then, the output should be: UPPER CASE 1 LOWER CASE 9

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

# Solution:
# s = input()
# d={"UPPER CASE":0, "LOWER CASE":0}
# for c in s:
#     if c.isupper():
#         d["UPPER CASE"]+=1
#     elif c.islower():
#         d["LOWER CASE"]+=1
#     else:
#         pass
# print("UPPER CASE", d["UPPER CASE"])
# print("LOWER CASE", d["LOWER CASE"])
####################################################


# s = input()
# ret = {'UPPER CASE' : 0, 'LOWER CASE' : 0}

# print(len(s))
# for i in range(0, len(s)):
#     if s[i].isupper():
#         ret['UPPER CASE'] += 1
#     elif s[i].islower():
#         ret['LOWER CASE'] += 1
#     else:
#         None

# print("UPPER", ret["UPPER CASE"])
# print("LOWER", ret["LOWER CASE"])

####################################################
# Question 15
# Level 2

# Question: Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a. 
# Suppose the following input is supplied to the program: 9 Then, the output should be: 11106

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

# Solution:
# a = input()
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# n4 = int( "%s%s%s%s" % (a,a,a,a) )
# print(n1+n2+n3+n4)
####################################################

# num = input()
# ret = 0
# a_s = num 
# aa_s = num * 2
# aaa_s = num * 3
# aaaa_s = num * 4

# ret = int(a_s) + int(aa_s) + int(aaa_s) + int(aaaa_s)

# print(ret)


####################################################
# Question 16
# Level 2

# Question: Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. 
# Suppose the following input is supplied to the program: 1,2,3,4,5,6,7,8,9 
# Then, the output should be: 1,3,5,7,9

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

# NOTE: comprehension to square is like this [str(x) for x in s.split(' ')] 

# Solution:
# values = input()
# numbers = [x for x in values.split(",") if int(x)%2!=0]
# print(",".join(numbers))
####################################################

# s = input()
# output_str = [str(x) for x in s.split(',') if int(x) % 2]     
# print(",".join(output_str))
# print(output_str)

####################################################
# Question 17
# Level 2

# Question: Write a program that computes the net amount of a bank account based a transaction log from console input. 
# The transaction log format is shown as following: D 100 W 200
# D means deposit while W means withdrawal. 
# Suppose the following input is supplied to the program: D 300 D 300 W 200 D 100 
# Then, the output should be: 500

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

# Solution:
# netAmount = 0
# while True:
#     s = input()
#     if not s:
#         break
#     values = s.split(" ")
#     operation = values[0]
#     amount = int(values[1])
#     if operation=="D":
#         netAmount+=amount
#     elif operation=="W":
#         netAmount-=amount
#     else:
#         pass
# print(netAmount)


# NOTE: Assume in real life when the user enter amount once for each deposit and withdraw
# Example: 
#       1st: Deposit 100 - Total 100
#       2nd: Deposit 100 - Total 200
#       3rd: Withdraw 200 - Total 0
####################################################

log = input()
digits = [str(x) for x in log.split(' ') if x.isdigit()]
modes = [str(x) for x in log.split(' ') if x.isalpha()]

total = 0

for i in range(0, len(modes)):
    if modes[i] == 'D':
        total += int(digits[i])
    elif modes[i] == 'W':
        total += int(digits[i])

print(total)





