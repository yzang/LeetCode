# encoding=UTF-8
__author__ = 'Vincent'



class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def singleNumber(self, nums):
        xory=0
        ans=reduce(lambda x,y:x^y,nums)

        return ans
a=[1,3,4,5,4,3,1,6,6]
solution=Solution()
print solution.singleNumber(a)
print 6&-6