## Assignment #2 ##

# Unit-tested Functions (Do NOT use python helper functions)
# - `func reverse(s: str) -> str` : take a string and return a string in reverse order.
# - Ex `reverse("abc")` returns `"cba"`
## Successful with Unit Testing ##
#----------------------------------------#
def reversestring(text):
    word_length = len(text)
    rev_word = ""
    for char in range(word_length):
        rev_word += text[ - 1 - char]
    return rev_word

# word = input("Enter a Word: ")
# print(reversestring(word))

#----------------------------------------#

#----------------------------------------#
# - `func reverse_in_place(s: str)` : take a string and modifies the string in-place.
# - Ex `s = "abc"; reverse_in_place(s)` after which s == `"cba"`
## UNIT TEST PASSED##

def reverse_in_place(text):
    s = ""
    word_len = len(text)
    index = word_len - 1
    while index >= 0:
        s += text[index]
        index -= 1
    return s

#---------------------------------------------#        

#------------------------------------------------------#

## Successful with Unit Testing ##
# - `func stutter(s: str, i: int) -> str`: multiply the letter of all consonants
# - `stutter("baby", 3)` = `"bbbabbbyyy"`

def stutter(word: str, i: int):
    vowels = ['a','e','i','o','u']
    s = ""
    for char in word:
        if char in vowels:
            s += char
        else:
            s += (char*i)
    return s

#-------------------------------------------------------#

#-------------------------------------------------------#

# - `func is_palindrome(s: str)-> bool`:  checks to see if a string is a palindrome
# - Version 1: for-loop
## UNIT TEST PASSED ##
def is_palindrome(s: str):
    text = ""
    for char in s:
        text = char + text
    if text == s:
        return True
    else:
        return False
# - Version 2: python indexing trick
def is_palindrome2(s: str):
    return s == s[::-1]

#-------------------------------------------------------#
print(is_palindrome2(input("Word...")))
#-------------------------------------------------------#
# - `func fact(n: int) -> int`  :  compute a factorial; `fact(5) = 5*4*3*2*1` or `fact(N) = N*(N-1)*(N-2)*...`
# - Version 1: for-loop

def factorial(n: int):
    if n == 0:
        return 1
    # else:
    x = 1
    for i in range(1, n+1):
        x *= i
    return x
    
        
        
        
    
# - Version 2: recursion

def recursive_factorial(n: int):
    if n == 0:
        return 1
    else:
        return n*recursive_factorial(n-1)
    

#-------------------------------------------------------#

#-------------------------------------------------------#
# - `func char_freq(s: str) -> dict[char, int]`: takes a string and puts out how many of each character there is.
# - Example: `char_freq("potato")` is `{ 'p': 1, 'o': 2, 't': 2, 'a': 1 }`
# - we can probably use this function along with matplotlib to actually create a histogram

def char_frequency(word: str):
    items = {}
    count = 0
    for char in word:
        items[char] = items.get(char, count) + 1
    return items

# word_to_add = char_frequency(input("What would you like to add? "))
# print(word_to_add)
        
        

#-------------------------------------------------------#

#-------------------------------------------------------#
# - `func word_count(s: str) -> dict[char, int]`: takes a file with several paragraphs of writing and puts out how many of each word there is. 
def identify_words (filename):
    with open(filename) as file:
        return file.read()

def wc(megaword: str):
    dic_wordcount = {}
    words = megaword.split()
    for word in words:
        dic_wordcount[word] = dic_wordcount.setdefault(word.strip(), 0) + 1
    return dic_wordcount

# wordle = identify_words("Paragraph.txt") 
# print(wc(wordle))    

# dictionary = identify_words("Paragraph.txt")
# print(dictionary)
