# encoding=UTF-8
__author__ = 'Vincent'
'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
-3,-2,-1,-1,-1,1,2
Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
先sort，然后用two pointers
'''
class Solution(object):
    def threeSum(self, nums):
        """
        two pointers problem
        first sort the list
        for each number, use two pointers point at the rest of the numbers
        if they add up less than or more than 0, move pointers
        """
        nums.sort()
        sumList=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            while left<right:
                sum_3=nums[i]+nums[left]+nums[right]
                if sum_3<0:
                    #then we have to increase, move the left pointer
                    #don't move L to much because we might miss
                    left+=1
                elif sum_3>0:
                    #then we have to decrease, move the right pointer
                    right-=1
                else:
                    sumList.append([nums[i],nums[left],nums[right]])
                    #then we look at whether we can reduce duplicated calculation
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
        return sumList

