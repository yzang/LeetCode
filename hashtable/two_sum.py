# encoding=UTF-8
__author__ = 'Vincent'
'''
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target,
where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}

    #change add problem into search problem
    def twoSum(self, nums, target):
        dict={}
        n=len(nums)
        for i in range(n):
            dict[nums[i]]=i
        for i in range(n):
            to_find=target-nums[i]
            pos=dict.get(to_find)
            if pos and pos!=i:
                if i<pos:
                    return [i+1,pos+1]
                else:
                    return [pos+1,i+1]



s=Solution()
res=s.twoSum([12,31,2,32,1,3,21,3],35)
print res