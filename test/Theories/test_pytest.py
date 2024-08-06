import pytest
from src.Theories.Python_practices import *
from io import StringIO

def test_increment(monkeypatch):
    number_input = StringIO('123\n')
    monkeypatch.setattr('sys.stdin', number_input)
    assert increment(number_input) == 124

def test_decrement(monkeypatch):
    number_input = StringIO('123')
    monkeypatch.setattr('sys.stdin', number_input)
    assert decrement(number_input) == 122

def test_check_division():
    # assert division_function()
    # assert ('2002' in division_function()) == 'True'
    if '2002' in division_function():
        assert True
    else:
        assert False

def test_fact():
    assert fact(10) == 3628800

def test_dicGen():
    assert dicGen(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    
@pytest.fixture
def test_genList_Tup():
    assert genList_Tup(5) == [[1, 2, 3, 4, 5], (1, 2, 3, 4, 5)]

def test_check_password(monkeypatch):
    password_input = StringIO("ABd1234@1\naF1#\n2w3E*\n2We3345\n")
    output_expected = 'ABd1234@1'
    monkeypatch.setattr('sys.stdin', password_input)
    assert check_password() == output_expected

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


    