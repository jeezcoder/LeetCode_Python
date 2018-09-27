class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        nums.sort(reverse=True)
        print (nums)
        for i in range(1,len(nums),2):
            sum += nums[i]
        return sum

if __name__ == '__main__':
    nums = [1,4,3,2]
    print(Solution().arrayPairSum(nums))

