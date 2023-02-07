def scoreOfParentheses(self, s: str) -> int:
        stack = []
        count=0
        for i in s:
            if i=="(":
                stack.append(i)
            elif i==")":
                count+=1

        return count