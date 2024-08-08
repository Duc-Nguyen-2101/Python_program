import pytest
from src.Theories.Python_practices import *
from io import StringIO
import random


def pytest_report_teststatus(report, config):
    if report.when == 'call':
        if report.skipped:
            return 's', 'skipped'
        if report.failed:
            return 'F', 'failed'
        if report.passed:
            return '.', 'passed'
    
        
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    terminalreporter.write_sep('=', 'test result')
    for rep in terminalreporter.stats.values():
        if rep.failed:
            terminalreporter.write('FAILED %s: %s\n' % (rep.nodeid, rep.outcome))
        if rep.passed:
            terminalreporter.write('PASSED %s\n' % rep.nodeid)
        if rep.skipped:
            terminalreporter.write('SKIPPED %s\n' % rep.node)

    terminalreporter.write_sep('=', 'end test result')

####################################################
# Simple function used to run pytest

####################################################
def test_increment(monkeypatch):
    number_input = StringIO('123\n')
    monkeypatch.setattr('sys.stdin', number_input)
    assert increment(number_input) == 124
    assert True

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
# Question 8
# Level 2

# Question: Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence 
# after sorting them alphabetically. Suppose the following input is supplied to the program: without,hello,bag,world 
# Then, the output should be: bag,hello,without,world
####################################################
def test_sortStr(monkeypatch):
    input_str = StringIO('without,hello,bag,world\n')
    expected_output = 'bag,hello,without,world'
    monkeypatch.setattr('sys.stdin', input_str)
    assert sort_str() == expected_output


####################################################
# Question 9
# Level 2

# Question£º Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized. 
# Suppose the following input is supplied to the program: Hello world Practice makes perfect 
# Then, the output should be: HELLO WORLD PRACTICE MAKES PERFECT
####################################################

def test_upperStr(monkeypatch):
    input_str = StringIO("hello")
    expected_output = 'HELLO'
    monkeypatch.setattr('sys.stdin', input_str)
    assert upper_str() == expected_output


####################################################
# Question 10
# Level 2

# Question: Write a program that accepts a sequence of whitespace separated words as input 
# and prints the words after removing all duplicate words and sorting them alphanumerically. 
# Suppose the following input is supplied to the program: hello world and practice makes perfect and hello world again 
# Then, the output should be: again and hello makes perfect practice world
####################################################
def test_removeDuplicate(monkeypatch):
    input_str = StringIO('hello world and practice makes perfect and hello world again\n')
    expected_output = 'again and hello makes perfect practice world'
    monkeypatch.setattr('sys.stdin', input_str)
    assert removeDuplicate() == expected_output


####################################################
# Question 11
# Level 2

# Question: Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and 
# then check whether they are divisible by 5 or not. 
# The numbers that are divisible by 5 are to be printed in a comma separated sequence. 
# Example: 0100,0011,1010,1001 Then the output should be: 1010 
# Notes: Assume the data is input by console.
####################################################
def test_division_binary(monkeypatch):
    input_str = StringIO('0100,0011,1010,1001\n')
    expected_output = '1010'
    monkeypatch.setattr('sys.stdin', input_str)
    assert division_binary() == expected_output


####################################################
# Question 12
# Level 2

# Question: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number. 
# The numbers obtained should be printed in a comma-separated sequence on a single line.
####################################################
def test_evenNumber():
    assert '2000' in even_number()


####################################################
# Question 13
# Level 2

# Question: Write a program that accepts a sentence and calculate the number of letters and digits. 
# Suppose the following input is supplied to the program: hello world! 123 
# Then, the output should be: LETTERS 10 DIGITS 3
####################################################
def test_countLetter(monkeypatch):
    input_str = StringIO('hello world! 123\n')
    expected_output = ('LETTERS 10', 'DIGITS 3', 'SPECIAL CHARACTER 1')
    monkeypatch.setattr('sys.stdin', input_str)
    assert count_letters() == expected_output



####################################################
# Question 14
# Level 2

# Question: Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters. 
# Suppose the following input is supplied to the program: Hello world! 
# Then, the output should be: UPPER CASE 1 LOWER CASE 9
####################################################

def test_countUpLowCase(monkeypatch):
    input_str = StringIO('Hello world!\n')
    expected_output = ('UPPER 1', 'LOWER 9')
    monkeypatch.setattr('sys.stdin', input_str)
    assert count_upper_lower() == expected_output


####################################################
# Question 15
# Level 2

# Question: Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a. 
# Suppose the following input is supplied to the program: 9 Then, the output should be: 11106
####################################################
def test_sum_digit(monkeypatch):
    input_str = StringIO("9")
    expected_output = 11106
    monkeypatch.setattr("sys.stdin", input_str)
    assert sum_digit() == expected_output


####################################################
# Question 16
# Level 2

# Question: Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. 
# Suppose the following input is supplied to the program: 1,2,3,4,5,6,7,8,9 
# Then, the output should be: 1,3,5,7,9
####################################################
def test_squareOdd(monkeypatch):
    input_str = StringIO("1,2,3,4,5,6,7,8,9")
    expected_output = ('1,3,5,7,9')
    monkeypatch.setattr("sys.stdin", input_str)
    assert square_odd() == expected_output


####################################################
# Question 17
# Level 2

# Question: Write a program that computes the net amount of a bank account based a transaction log from console input. 
# The transaction log format is shown as following: D 100 W 200
# D means deposit while W means withdrawal. 
# Suppose the following input is supplied to the program: D 300 D 300 W 200 D 100 
# Then, the output should be: 500

# NOTE: Assume in real life when the user enter amount once for each deposit and withdraw
# Example: 
#       1st: Deposit 100 - Total 100
#       2nd: Deposit 100 - Total 200
#       3rd: Withdraw 200 - Total 0
####################################################
def test_bank_account(monkeypatch):
    input_str = StringIO('D 300\nD 300\nW 200\nD 100\n\n')
    expected_output = 500 # Replace with the actual expected result
    monkeypatch.setattr('sys.stdin', input_str)
    assert bank_account() == expected_output


# Test upgrade version
def test_mode(monkeypatch):
    input_str = StringIO("D")
    expected_output = "D"
    monkeypatch.setattr("sys.stdin", input_str)
    assert mode() == expected_output

def test_amountCal(monkeypatch):
    mode_input = StringIO("D")
    amount_input = 1000
    expected_output = 1000
    monkeypatch.setattr("sys.stdin", mode_input)
    assert amount_cal(mode_input, amount_input) == expected_output

class TestGroup_Question17:
    def test_bankAccount_1(self, monkeypatch):
        test_input = StringIO("D\n1000\nN\n")
        expected_output = 1000
        monkeypatch.setattr("sys.stdin", test_input)
        assert bank_account_2() == expected_output

    def test_bankAccount_2(self, monkeypatch):
        test_input = StringIO("D\n1000\nY\nW\n111\nN\n")
        expected_output = 889
        monkeypatch.setattr("sys.stdin", test_input)
        assert bank_account_2() == expected_output

    def test_bankAccount_3(self, monkeypatch):
        test_input = StringIO("123\n")
        expected_output = 0
        monkeypatch.setattr("sys.stdin", test_input)
        assert bank_account_2() == expected_output
        
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
class TestGroup_Question18:
    def test_check_password_1(self, monkeypatch):
        password_input = StringIO("ABd1234@1\naF1#\n2w3E*\n2We3345\n")
        output_expected = 'ABd1234@1'
        monkeypatch.setattr('sys.stdin', password_input)
        assert check_password() == output_expected
    
    def test_check_password_2(self, monkeypatch):
        password_input = StringIO("aF1#\n2w3E*\n2We3345\n")
        output_expected = None
        monkeypatch.setattr('sys.stdin', password_input)
        assert check_password() == output_expected

    def test_check_password_3(self, monkeypatch):
        password_input = StringIO("ABd4@\n2w3E*\n2We3345\n")
        output_expected = None
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
def test_sort_function(monkeypatch):
    input_str = StringIO('Tom,19,80\nJohn,20,90\nBob,17,91\nJony,17,93\nAlex,21,85\n\n')
    expected_output = [
        ('Alex','21','85'),
        ('Bob','17','91'),
        ('John','20','90'),
        ('Jony','17','93'),
        ('Tom','19','80')
    ]  # Replace with the actual expected result
    monkeypatch.setattr('sys.stdin', input_str)
    assert sort_function() == expected_output


    