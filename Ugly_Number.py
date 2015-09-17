# encoding=UTF-8
__author__ = 'Vincent'

'''
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
 For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.
'''

class Solution:
    # @param {integer} num
    # @return {boolean}
    def isUgly(self, num):
        while num!=0:
            if num==1:
                break
            else:
                if num%5==0:
                    num/=5
                elif num%3==0:
                    num/=3
                elif num%2==0:
                    num/=2
                else:
                    break
        return num==1

solution=Solution()
print solution.isUgly(150)