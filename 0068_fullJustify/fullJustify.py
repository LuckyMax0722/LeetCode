class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        temp = ''
        sentence_len = 0
        count = 0
        ans = []
        num_words = []

        for i in range(len(words)):
            word_len = len(words[i])

            if (sentence_len + word_len) <= maxWidth:
                sentence_len = sentence_len + word_len + 1
                temp = temp + words[i] + ' '
                count = count + 1
            else:
                # 处理空格问题
                temp = temp[0:-1]
                n = len(temp)
                diff = maxWidth - n
                margin = count - 1

                if margin != 0 and diff % margin == 0:
                    add = [diff / margin for _ in range(margin)]
                elif margin != 0 and diff % margin != 0:
                    add = [0 for _ in range(margin)]
                    idx = 0
                    while idx < diff:
                        add[idx % margin] = add[idx % margin] + 1
                        idx = idx + 1
                elif margin == 0:
                    add = [diff]

                word_end = False
                word_add = False
                point = 0

                for idx in range(maxWidth):
                    if margin == 0 and not word_add:
                        temp = list(temp)
                        for _ in range(add[point]):
                            temp.append(' ')
                        temp = ''.join(temp)
                        word_add = True

                    elif temp[idx] == ' ' and not word_end and margin != 0:
                        word_end = True
                        temp = list(temp)  # 字符串转list
                        for _ in range(add[point]):
                            temp.insert(idx, ' ')  # 在指定位置插入字符串
                        temp = ''.join(temp)
                        point = point + 1

                    elif temp[idx] != ' ' and word_end:
                        word_end = False

                ans.append(temp)

                temp = ''
                sentence_len = word_len + 1
                temp = temp + words[i] + ' '
                count = 1

        temp = temp[0:-1]
        n = len(temp)
        diff = maxWidth - n
        temp = list(temp)  # 字符串转list

        for _ in range(diff):
            temp.append(' ')  # 在指定位置插入字符串
        temp = ''.join(temp)
        ans.append(temp)

        return ans


