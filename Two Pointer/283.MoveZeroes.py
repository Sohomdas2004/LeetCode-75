"""
LeetCode Problem No 283:Move Zeroes(https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75)

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

"""

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        index=0

        while i<len(nums):
            if nums[i]!=0:
                nums[index]=nums[i]
                index+=1
            i+=1

        while index<len(nums):
            nums[index]=0
            index+=1

        # count=0
        # res=[]
        
        # for i in nums:
        #     if(i!=0):
        #         res.append(i)
        #         count+=1
        
        # for count in range(len(nums)):
        #     res.append(0)
        
        # for i in range(len(nums)):
        #     nums[i]=res[i]