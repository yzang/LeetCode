# encoding=UTF-8
__author__ = 'Vincent'

'''
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number.

'''

class Solution:
    # @param {integer} num
    # @return {boolean}
    def nthUglyNumber(self, n):
        ugly=[1]
        p2=0
        p3=0
        p5=0
        while len(ugly)<n:
            nextUgly=min(ugly[p2]*2,ugly[p3]*3,ugly[p5]*5)
            if nextUgly>ugly[-1]:
                ugly.append(nextUgly)
            if nextUgly==ugly[p2]*2:
                p2+=1
            elif nextUgly==ugly[p3]*3:
                p3+=1
            else:
                p5+=1
        return ugly[-1]

solution=Solution()
print solution.nthUglyNumber(8)