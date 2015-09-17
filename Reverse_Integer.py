# encoding=UTF-8
__author__ = 'Vincent'
'''
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''

class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        overflow_point=pow(2,31)
        minus=False
        if x<0:
            minus=True
        x=abs(x)
        x_str=str(x)
        if (not x_str[len(x_str)-1]=='0') and len(x_str)>len(str(overflow_point)):
            return 0
        reversed_result=0
        times=1
        for digit in x_str:
            num=int(digit)
            reversed_result+=num*times
            times*=10
        if reversed_result>overflow_point:
            return 0
        if minus:
            reversed_result=-reversed_result
        return reversed_result

solution=Solution()
print solution.reverse(1234005)