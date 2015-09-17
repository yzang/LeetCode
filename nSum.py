# encoding=UTF-8
__author__ = 'Vincent'
'''
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
用nsum来做,先排序再递归,直到N=2时用two pointers
'''
class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        self.result=[]
        self.nSum(nums,4,target,[])
        return self.result


    def nSum(self,nums,N,target,tempResult):
        #two sum
        if len(nums)<N or N<2:
            return
        if N==2:
            L=0
            R=len(nums)-1
            while L<R:
                if nums[L]+nums[R]==target:
                    self.result.append(tempResult+[nums[L],nums[R]])
                    while L<R and nums[L]==nums[L+1]:
                        L+=1
                    while L<R and nums[R]==nums[R-1]:
                        R-=1
                    L+=1
                    R-=1
                elif nums[L]+nums[R]<target:
                    L+=1
                else:
                    R-=1

        else:
            for i in range(len(nums)-N+1):
                if nums[i]*N>target or nums[-1]*N<target:
                    break
                if i>0 and nums[i]==nums[i-1]:
                    continue
                self.nSum(nums[i+1:],N-1,target-nums[i],tempResult+[nums[i]])
        return

