from typing import List
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        in_block = False
        res = []
        for each_line in source:
            i = 0
            newline = []
            while i < len(each_line):
                if each_line[i:i + 2] == '/*' and not in_block:
                    in_block = True
                    i += 1
                elif each_line[i:i + 2] == '*/' and in_block:
                    in_block = False
                    i += 1
                elif not in_block and each_line[i:i + 2] == '//':
                    break
                elif not in_block:
                    newline.append(each_line[i])

                i += 1

            if not in_block and newline:
                res.append(''.join(newline))

        return res