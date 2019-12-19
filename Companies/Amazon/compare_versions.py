class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        v1_segments = v1.split('.')
        v2_segments = v2.split('.')

        i = 0
        j = 0

        while i < len(v1_segments) and j < len(v2_segments):
            diff = int(v1_segments[i]) - int(v2_segments[j])
            if diff < 0:
                return -1
            elif diff > 0:
                return 1
            i += 1
            j += 1

        if i < len(v1_segments):
            # if i has more elements
            return 1 if any([int(x) for x in v1_segments[i:]]) else 0
        elif j < len(v2_segments):
            # if j has more elements
            return -1 if any([int(y) for y in v2_segments[j:]]) != 0 else 0
        return 0


s = Solution()
print(s.compareVersion('1.01', '1.001'))
