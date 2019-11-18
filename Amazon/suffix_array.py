"""
Get the suffix array of the given string.

Used for
1. pattern finding
2. Largest Duplicate SubString
3. Largest Repeating Substring
"""


def suffix_array(s):
    suf_array_map = {i: s[i: ] for i in range(len(s))}
    print(suf_array_map)
    return [x for x, _ in sorted(suf_array_map.items(), key=lambda x: x[1])] # sort based of the string and return the x


print(suffix_array("ABRACADABRA"))
