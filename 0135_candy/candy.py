class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int


        candy_num = [1 for _ in range(len(ratings))]

        for idx in range(len(ratings) - 1):
            if ratings[idx] > ratings[idx + 1]:
                candy_num[idx] = max(candy_num[idx + 1] + 1, candy_num[idx])
            elif ratings[idx] < ratings[idx + 1]:
                candy_num[idx + 1] = max(candy_num[idx] + 1, candy_num[idx + 1])

        reverse_ratings = ratings[::-1]
        candy_num_reverse = [1 for _ in range(len(ratings))]

        for idx in range(len(reverse_ratings) - 1):
            if reverse_ratings[idx] > reverse_ratings[idx + 1]:
                candy_num_reverse[idx] = max(candy_num_reverse[idx + 1] + 1, candy_num_reverse[idx])
            elif reverse_ratings[idx] < reverse_ratings[idx + 1]:
                candy_num_reverse[idx + 1] = max(candy_num_reverse[idx] + 1, candy_num_reverse[idx + 1])

        candy_num_reverse = candy_num_reverse[::-1]

        result = [max(x, y) for x, y in zip(candy_num, candy_num_reverse)]

        return sum(result)

        #笨办法，遍历两次，左向右，右向左
        """

        candy_num = [1 for _ in range(len(ratings))]

        for idx in range(len(ratings) - 1):
            if ratings[idx] < ratings[idx + 1]:
                candy_num[idx + 1] = max(candy_num[idx] + 1, candy_num[idx + 1])

        reverse_ratings = ratings[::-1]
        candy_num_reverse = [1 for _ in range(len(ratings))]

        for idx in range(len(reverse_ratings) - 1):
            if reverse_ratings[idx] < reverse_ratings[idx + 1]:
                candy_num_reverse[idx + 1] = max(candy_num_reverse[idx] + 1, candy_num_reverse[idx + 1])

        candy_num_reverse = candy_num_reverse[::-1]

        result = [max(x, y) for x, y in zip(candy_num, candy_num_reverse)]

        return sum(result)
        # 笨办法，遍历两次，左向右，右向左
        # 优化版--> 我们只需要考虑同方向的递增情况，递减可由另一方向考虑

    # 官方解答给了一个递增递减的思考方法，不会