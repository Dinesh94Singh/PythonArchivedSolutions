class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        i = 0
        while i < len(s):
            print(stack)
            if i == 0 or s[i] != s[i - 1]:
                stack.append(1)
                i += 1
            else:
                prev_count = stack.pop()

                if prev_count + 1 == k:
                    s = s[:i - k + 1] + s[i+1:]
                    i = i - k + 1
                else:
                    stack.append(prev_count + 1)
                    i += 1
        return s
    
s = Solution()
print(s.removeDuplicates("deeedbbcccbdaa", 3))