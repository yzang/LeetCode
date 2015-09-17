# encoding=UTF-8
__author__ = 'Vincent'
'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"

'''
class Solution(object):
    def generateParenthesis(self, n):
        self.results=[]
        self.dfs(n,n,"")
        return self.results

    # if left has remain>0, then we can add left (
    # if right remain<left remain, then we can add right )
    def dfs(self,l_remain,r_remain,path):
        if l_remain==0 and r_remain==0:
            self.results.append(path)
            return
        if l_remain>0:
            self.dfs(l_remain-1,r_remain,path+"(")
        if r_remain>l_remain and r_remain>0:
            self.dfs(l_remain,r_remain-1,path+")")
