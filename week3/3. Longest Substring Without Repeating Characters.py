# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# s = "dvdf"
s = "pwwkew"
# s = "anviaj"
LEN = len(s)
dy_list = LEN * [0]
last_index = 0

LEN = len(s)
dy_list = LEN * [0]
last_index = 0

for i in range(LEN):
    if i == 0:
        dy_list[0] = 1
    else:
        if (i - last_index + 1) == len(set(s[last_index : i + 1])):
            dy_list[i] = dy_list[i - 1] + 1
        else:
            # 여기서 중복이 아닌 시점을 찾아서 돌아가야한다.
            if s[i] == s[i - 1]:
                dy_list[i] = 1
                last_index = i
            else:
                new_index = s[last_index : i + 1].index(s[i])
                dy_list[i] = dy_list[new_index + 1]
                last_index = new_index + 1

if dy_list:
    print(max(dy_list))
else:
    print(0)

"""
i = 1
last_index = 0
1 - 0 + 1 = 2
s[1:
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [None] * 128

        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]

            index = chars[ord(r)]
            if index is not None and left <= index < right:
                left = index + 1

            res = max(res, right - left + 1)

            chars[ord(r)] = right
            right += 1
        return res


# https://leetcode.com/problems/longest-substring-without-repeating-characters/solutions/127839/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans
