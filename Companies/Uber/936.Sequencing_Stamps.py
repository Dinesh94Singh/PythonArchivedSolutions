from typing import List


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        def can_replace(pos, stamp, target):
            for i in range(len(stamp)):
                if target[pos + i] != '*' and stamp[i] != target[pos + i]:
                    return False
            return True

        def replace(pos, stamp_length, target, total_stars):
            count = total_stars
            for i in range(stamp_length):
                if target[pos + i] != '*':
                    count += 1
                    target[pos + i] = '*'

            return count

        stamp = list(stamp)
        target = list(target)

        stamp_length = len(stamp)
        target_length = len(target)

        visited = [False for _ in range(target_length)]

        total_stars = 0
        result = []
        while total_stars < target_length:
            able_to_replace_in_the_run = False
            for i in range(target_length - stamp_length + 1):
                if not visited[i] and can_replace(i, stamp, target):
                    total_stars = replace(i, stamp_length, target, total_stars)
                    result.append(i)
                    able_to_replace_in_the_run = True
                    visited[i] = True
                    print(total_stars, target)
                    if total_stars == target_length:
                        break

            if not able_to_replace_in_the_run:
                return []

        return result[::-1]


s = Solution()
print(s.movesToStamp("abc", "ababc"))