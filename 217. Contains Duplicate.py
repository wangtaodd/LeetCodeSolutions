"""Given an array of integers, find if the array contains any duplicates. Your function should return true if any valueappears at least twice in the array, and it should return false if every element is distinct."""class Solution(object):    def containsDuplicate(self, nums):        """        :type nums: List[int]        :rtype: bool        """        if not nums: return False        nDict={}        for i in nums:            try:                nDict[i]+=1                return True            except:                nDict[i]=1        return False