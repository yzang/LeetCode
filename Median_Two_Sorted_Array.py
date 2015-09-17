# encoding=UTF-8
__author__ = 'Vincent'
'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

1,5,6,7,9,10
8,9,11,16,20,21


'''
class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        mergeResult=self.mergeSort(nums1,nums2)
        if len(mergeResult)%2==0:
            return (mergeResult[len(mergeResult)/2-1]+mergeResult[len(mergeResult)/2])/2.0
        else:
            return mergeResult[len(mergeResult)/2]

    def mergeSort(self,num1,num2):
        result=[]
        i=j=0
        while i<len(num1) and j<len(num2):
            if num1[i]<num2[j]:
                result.append(num1[i])
                i+=1
            else:
                result.append(num2[j])
                j+=1
        while i<len(num1):
            result.append(num1[i])
            i+=1
        while j<len(num2):
            result.append(num2[j])
            j+=1
        return result

solution=Solution()
print solution.findMedianSortedArrays([],[2,15])