class Solution:
    def restoreIpAddresses(self, s):
        def valid(segment):
            return int(segment) <= 255 if segment[0] != '0' else len(segment) == 1

        def update_output(curr_pos):
            segment = s[curr_pos + 1:n]
            if valid(segment):
                segments.append(segment)
                output.append('.'.join(segments))
                segments.pop()

        def backtrack(prev_pos=-1, dots=3):
            for curr_pos in range(prev_pos + 1, min(n - 1, prev_pos + 4)):
                segment = s[prev_pos + 1:curr_pos + 1]
                if valid(segment):
                    segments.append(segment)  # place dot
                    if dots - 1 == 0:  # if all 3 dots are placed
                        update_output(curr_pos)  # add the solution to output
                    else:
                        backtrack(curr_pos, dots - 1)  # continue to place dots
                    segments.pop()  # remove the last placed dot
        n = len(s)
        output, segments = [], []
        backtrack()
