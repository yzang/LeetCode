# encoding=UTF-8
__author__ = 'Vincent'

'''
Determine whether an integer is a palindrome. Do this without extra space.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer",
you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
'''

class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        reversed_num=0
        y=x
        if x<0:
            return False
        while not y==0:
            digit= y%10
            reversed_num=reversed_num*10+digit
            y=y/10
        if reversed_num==x:
            return True
        else:
            return False

solution=Solution()
print solution.isPalindrome(1)
