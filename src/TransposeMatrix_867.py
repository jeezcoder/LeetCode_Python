class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        row_cnt = len(A)
        col_cnt = len(A[0])

        ret = [list() for i in range(col_cnt)]
        
        for i in range(row_cnt):
            for j in range(col_cnt):
                ret[j].append(A[i][j])
        return ret




if __name__ == "__main__":
    s = Solution()
    A = [[1,2,3], [4,5,6],[7,8,9]]
    #A = [[1,2,3],[4,5,6]]
    print(s.transpose(A))

