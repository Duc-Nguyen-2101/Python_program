import pytest
from src.Theories.Python_practices import *
from io import StringIO
import random

def test_increment(monkeypatch):
    number_input = StringIO('123\n')
    monkeypatch.setattr('sys.stdin', number_input)
    assert increment(number_input) == 124

def test_decrement(monkeypatch):
    number_input = StringIO('123')
    monkeypatch.setattr('sys.stdin', number_input)
    assert decrement(number_input) == 122

####################################################
# Question 1
# Level 1

# Question: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
# between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.
####################################################
def test_check_division():
    # assert division_function()
    # assert ('2002' in division_function()) == 'True'
    if '2002' in division_function():
        assert True
    else:
        assert False

####################################################
# Question 2
# Level 1

# Question: Write a program which can compute the factorial of a given numbers. 
# The results should be printed in a comma-separated sequence on a single line. 
# Suppose the following input is supplied to the program: 8 Then, the output should be: 40320
####################################################
def test_fact():
    assert fact(10) == 3628800

####################################################
# Question 3
# Level 1

# Question: With a given integral number n, write a program to generate a dictionary that contains (i, i*i) 
# such that is an integral number between 1 and n (both included). and then the program should print the dictionary. 
# Suppose the following input is supplied to the program: 8 Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
####################################################
def test_dicGen():
    assert dicGen(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


####################################################
# Question 4
# Level 1

# Question: Write a program which accepts a sequence of comma-separated numbers from console 
# and generate a list and a tuple which contains every number. 
# Suppose the following input is supplied to the program: 34,67,55,33,12,98 
# Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')
####################################################
def test_genList_Tup():
    assert genList_Tup(5)

####################################################
# Question 5
# Level 1

# Question: Define a class which has at least two methods: 
# getString: to get a string from console input printString: to print the string in upper case. 
# Also please include simple test function to test the class methods.

# Hints: Use init method to construct some parameters
####################################################
def test_InOutStr(monkeypatch):
    def test_getStr():
        test = Solution()
        assert test.getStr() == 'Hello'
    
    def test_printStr():
        test = Solution()
        assert test.printString() == 'HELLO'

####################################################
# Question 6
# Level 2

# Question: Write a program that calculates and prints the value according to the given formula: 

# Q = Square root of [(2 * C * D)/H] 

# Following are the fixed values of C and H: C is 50. H is 30. 
# D is the variable whose values should be input to your program in a comma-separated sequence. 
# Example Let us assume the following comma separated input sequence is given to the program: 100,150,180 
# The output of the program should be: 18,22,24
####################################################
def test_calculation():
    assert squareRoot(100) == 18
    assert squareRoot(150) == 22
    assert squareRoot(180) == 24


####################################################
# Question 7
# Level 2

# Question: Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
# The element value in the i-th row and j-th column of the array should be i*j. Note: i=0,1.., X-1; j=0,1,¡­Y-1. 
# Example Suppose the following inputs are given to the program: 3,5 
# Then, the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
####################################################
def test_arrGen():
    assert arrayGen(3,5) == [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]











####################################################
# Question 18
# Level 3

# Question: A website requires the users to input username and password to register. 
# Write a program to check the validity of password input by users. 
# Following are the criteria for checking the password:

# At least 1 letter between [a-z]
# At least 1 number between [0-9]
# At least 1 letter between [A-Z]
# At least 1 character from [$#@]
# Minimum length of transaction password: 6
# Maximum length of transaction password: 12 Your program should accept a sequence of comma separated passwords 
# and will check them according to the above criteria. 
# Passwords that match the criteria are to be printed, each separated by a comma. 
# Example If the following passwords are given as input to the program: "ABd1234@1","aF1#","2w3E*","2We3345"
# Then, the output of the program should be: "ABd1234@1"
####################################################
def test_check_password(monkeypatch):
    password_input = StringIO("ABd1234@1\naF1#\n2w3E*\n2We3345\n")
    output_expected = 'ABd1234@1'
    monkeypatch.setattr('sys.stdin', password_input)
    assert check_password() == output_expected











####################################################
# Question 19
# Level 3

# Question: You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers.
# The tuples are input by console. The sort criteria is: 1: Sort based on name; 2: Then sort based on age; 3: 
# Then sort by score. The priority is that name > age > score. 
# If the following tuples are given as input to the program: Tom,19,80 John,20,90 Jony,17,91 Jony,17,93 Json,21,85 
# Then, the output of the program should be: [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
####################################################
@pytest.fixture
def test_sort_function(monkeypatch):
    input_str = StringIO('Tom,19,80\nJohn,20,90\nBob,17,91\nJony,17,93\nAlex,21,85\n')
    expected_output = [
        ('Alex','21','85'),
        ('Bob','17','91'),
        ('John','20','90'),
        ('Jony','17','93'),
        ('Tom','19','80')
    ]  # Replace with the actual expected result
    monkeypatch.setattr('sys.stdin', input_str)
    # monkeypatch.setattr("builtins.input", lambda _: "Tom,19,80\nJohn,20,90\nBob,17,91\nJony,17,93\nAlex,21,85\n")
    assert sort_function() == expected_output


    