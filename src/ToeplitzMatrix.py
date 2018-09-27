class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        nums = []
        for row in matrix:
            nums.extend(row)
        nums_max_index = len(nums) - 1
        row_len = len(matrix[0])
        for i in range(len(nums)):
            next_index = i + row_len + 1
            if (i+1) % row_len != 0 and   next_index <= nums_max_index and nums[i]  != nums[next_index]:
                return False
        return True

            




if __name__ == "__main__":

    matrix = [ [1,2,3,4],
               [5,1,2,3],
               [9,5,1,2] ]
    print(Solution().isToeplitzMatrix(matrix))

