class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roma_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40,
                     'XC': 90, 'CD': 400, 'CM': 900}

        ans = 0

        n = len(s)
        idx = 0

        while idx < n:
            cur_1 = s[idx]
            cur_2 = s[idx] + s[idx + 1] if idx + 1 < n else s[idx]

            if cur_2 in roma_dict:
                ans = ans + roma_dict[cur_2]
                idx = idx + 2
            else:
                ans = ans + roma_dict[cur_1]
                idx = idx + 1

        return ans

        """
        # 好好好，这样玩是吧
        class Solution {
            public int romanToInt(String s) {
                s = s.replace("IV","a");
                s = s.replace("IX","b");
                s = s.replace("XL","c");
                s = s.replace("XC","d");
                s = s.replace("CD","e");
                s = s.replace("CM","f");

                int result = 0;
                for (int i=0; i<s.length(); i++) {
                    result += which(s.charAt(i));
                }
                return result;
            }

            public int which(char ch) {
                switch(ch) {
                    case 'I': return 1;
                    case 'V': return 5;
                    case 'X': return 10;
                    case 'L': return 50;
                    case 'C': return 100;
                    case 'D': return 500;
                    case 'M': return 1000;
                    case 'a': return 4;
                    case 'b': return 9;
                    case 'c': return 40;
                    case 'd': return 90;
                    case 'e': return 400;
                    case 'f': return 900;
                }
                return 0;
            }
        }
        """
