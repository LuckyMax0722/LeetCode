class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        cur_list = [1]
        res.append(cur_list)

        def generateList(i, cur_list):
            res_list = [0] * (i + 1)
            for j in range(i + 1):
                if j == 0:
                    res_list[0] = cur_list[0]
                elif j == i:
                    res_list[-1] = cur_list[-1]
                else:
                    res_list[j] = cur_list[j] + cur_list[j - 1]

            return res_list

        for i in range(1, numRows):
            cur_list = generateList(i, cur_list)
            res.append(cur_list)

        return res


