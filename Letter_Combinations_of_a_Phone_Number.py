# encoding=UTF-8
__author__ = 'Vincent'
'''
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''


def dicarrel(x,y):
    combined=[]
    for c_i in x:
        for c_j in y:
            combined.append(c_i+c_j)
    return combined

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        reduced=[]
        if digits:
            dict=[[''],['_'],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
            mapped=map(lambda x:dict[int(x)], digits)
            reduced=reduce(dicarrel,mapped)
        return reduced

solution=Solution()
solution.letterCombinations("123")