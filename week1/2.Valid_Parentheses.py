# https://leetcode.com/problems/valid-parentheses/
# 스택 사용

s = "((({[]})))"

bracket_check_dict = {")": "(", "]": "[", "}": "{"}


class Solution:
    def isValid(self, s: str) -> bool:
        S = []
        for x in s:
            if x in ["(", "[", "{"]:
                S.insert(0, x)
            else:
                if S:
                    pop_value = S.pop(0)
                    if bracket_check_dict[x] == pop_value:
                        pass
                    else:
                        return False
                else:
                    return False
        if S:
            return False
        else:
            return True


func = Solution()
func.isValid(s=s)
