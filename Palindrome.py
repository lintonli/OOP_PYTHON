#using class
class IsPalindrome:
    def __init__(self, word):
        self.word = word
    def is_palindrome(self):
        self.word = self.word.lower()
        reversed_word=""
        for i in self.word:
            reversed_word = i + reversed_word
        return reversed_word == self.word
palindrome = IsPalindrome("madam")
print(palindrome.is_palindrome())

#using function only

def is_palindrome(word):
    word = word.lower()
    palindrome_word= ""

    for i in word:
        palindrome_word = i + palindrome_word
    return palindrome_word == word
print(is_palindrome("wow"))

