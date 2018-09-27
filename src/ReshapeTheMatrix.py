class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        nums_len = len(nums)
        ele_cnt = len(nums[0]) * nums_len
        if r *c != ele_cnt:
            return nums
        ret = []
        i = 0
        temp = []
        for row in nums:
            for ele in row:
                temp.append(ele)
                if (i + 1) % c == 0:
                    ret.append(temp)
                    temp = []
                i += 1
        return ret


class Solution2:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r *c != len(nums) * len(nums[0]):
            return nums
        num_list = []
        for num in nums:
            num_list.extend(num)
        ret = []
        for i in range(r):
            ret.append(num_list[i*c:i*c+c])
        return ret
if __name__ == "__main__":
    nums =[[1,2],[3,4]]
    r = 1
    c = 4
    print(Solution2().matrixReshape(nums, r, c))


