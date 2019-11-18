def longest_common_prefix_array(s):
    def suffix_array(s):
        suf_array_map = {i: s[i:] for i in range(len(s))}
        return [suf_array for suf_array in
                sorted(suf_array_map.items(), key=lambda x: x[1])]

    def get_common_prefix(s1, s2):
        for i in range(min(len(s1), len(s2))):
            if s1[i] != s2[i]:
                return i + 1
        return i + 1

    suffix_array_matrix = suffix_array(s)
    print(suffix_array_matrix)

    res = [0]
    for i in range(1, len(suffix_array_matrix)):
        c = get_common_prefix(suffix_array_matrix[i - 1][1], suffix_array_matrix[i][1])
        res.append(c)

    return res


print(longest_common_prefix_array('ABRACADABRA'))
