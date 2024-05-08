
import pytest
import Assignment
from unittest import TestCase

def test_reverse():
    output = Assignment.reversestring('row')
    assert output == 'wor'
def test_reverse2():
    output = Assignment.reversestring('wonder')
    assert output == 'rednow'    
def test_reverse3():
    output = Assignment.reversestring('articulate')
    assert output == 'etalucitra'
def test_reverse4():
    output = Assignment.reversestring('ranger')
    assert output == 'regnar'
def test_reverse5():
    output = Assignment.reversestring('aardvark')
    assert output == 'kravdraa'
def test_reverse6():
    output = Assignment.reversestring('')
    assert output == ''
    
def test_rev_in_place():
    output = Assignment.reverse_in_place('row')
    assert output == 'wor'
def test_rev_in_place2():
    output = Assignment.reverse_in_place('wonder')
    assert output == 'rednow'    
def test_rev_in_place3():
    output = Assignment.reverse_in_place('articulate')
    assert output == 'etalucitra'
def test_rev_in_place4():
    output = Assignment.reverse_in_place('ranger')
    assert output == 'regnar'
def test_rev_in_place5():
    output = Assignment.reverse_in_place('aardvark')
    assert output == 'kravdraa'

def test_stutter():
    output = Assignment.stutter('row',0)
    assert output == 'o'
def test_stutter2():
    output = Assignment.stutter('wonder',3)
    assert output == 'wwwonnnddderrr'    
def test_stutter3():
    output = Assignment.stutter('articulate',3)
    assert output == 'arrrttticcculllattte'
def test_stutter4():
    output = Assignment.stutter('ranger',5)
    assert output == 'rrrrrannnnngggggerrrrr'
def test_stutter5():
    output = Assignment.stutter('aardvark',-1)
    assert output == 'aaa'

def test_isPalindrome():
    output = Assignment.is_palindrome('row')
    assert output == False
def test_isPalindrome2():
    output = Assignment.is_palindrome('noon')
    assert output == True    
def test_isPalindrome3():
    output = Assignment.is_palindrome('racecar')
    assert output == True
def test_isPalindrome4():
    output = Assignment.is_palindrome('spooky')
    assert output == False
def test_isPalindrome5():
    # output = Assignment.is_palindrome('asdfgfdsa')
    assert Assignment.is_palindrome2('asdfgfdsa') == True
    assert Assignment.is_palindrome2('asldkfjaoivinawioefjl;ifj;s') == False
    assert Assignment.is_palindrome2('asdfgfdifdsiida') == True
    
def test_factorial():
    output = Assignment.factorial(1)
    assert output == 1
    output = Assignment.factorial(2)
    assert output == 2
    output = Assignment.factorial(3)
    assert output == 6
    output = Assignment.factorial(4)
    assert output == 24
    output = Assignment.factorial(0)
    assert output == 1

    
def test_rec_factorial():
    output = Assignment.recursive_factorial(1)
    assert output == 1
    output = Assignment.recursive_factorial(2)
    assert output == 2
    output = Assignment.recursive_factorial(3)
    assert output == 6
    output = Assignment.recursive_factorial(4)
    assert output == 24
    output = Assignment.recursive_factorial(0)
    assert output == 1

# @pytest.mark.parametrize("word_tups", "count",
#     [ 
#       (("terry is amazing!", "i"), 2)
#     ]
# )
# def test_char_freq(word_tups, count):
#     freq = Assignment.char_frequency(word_tups[0])
#     assert freq[word_tups[1]] == count

def test_char_freq():
    freqs = Assignment.char_frequency("terry is amazing! ")
    assert freqs["i"] == 2
    assert freqs["t"] == 1
    assert freqs[" "] == 3
    assert freqs["r"] == 2
    
def test_wc():
    freqs = Assignment.wc("one two three one one three")
    assert freqs["one"] == 3

pytest.main(["As2test.py"])