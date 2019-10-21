"""
Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict.
If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are
consecutive, you need to combine them.
Example 1:

Input:
s = "abcxyz123"
dict = ["abc","123"]
Output:
"<b>abc</b>xyz<b>123</b>"
Example 2:

Input:
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"<b>aaabbc</b>c"
Note:

Input:
s = "aaabbcc"
dict = ["a","b","c"]
Output:
"<b>aaabbcc</b>"

Input:
s = "abcdef"
dict = ["a","c","e","g"]
Output:
"<b>a</b>b<b>c</b>d<b>e</b>f"

The given dict won't contain duplicates, and its length won't exceed 100.
All the strings in input have length in range [1, 1000].
"""


def add_bold_tag(s, dic):
    l = list(s)
    start_index = 0
    intervals = []
    if len(dic) == 0:
        return s
    while start_index < len(l):
        end_index = start_index
        while end_index < len(l):
            sub_string = ''.join(l[start_index: end_index + 1])
            if sub_string in dic:
                intervals.append([start_index, end_index])
            end_index += 1
        start_index += 1
    # print('intervals is', intervals)

    # perform merge intervals

    if len(intervals) == 0:
        return s

    start = intervals[0][0]
    end = intervals[0][1]
    res = []
    for idx in range(1, len(intervals)):
        # a overlaps b or b overlaps a or [0, 3],[4, 5] => [0, 5]
        if (end >= intervals[idx][0]) or (end+1 == intervals[idx][0]):
            end = max(end, intervals[idx][1])
        else:
            res.append([start, end])
            start = intervals[idx][0]
            end = intervals[idx][1]
    res.append([start, end])
    # print(res)

    # add the tags

    i = 0
    pair = res[0]
    result = ''
    for idx, each in enumerate(l):
        # print(pair)
        if pair[0] == pair[1] == idx:
            result += '<b>'
            result += each
            result += '</b>'
            i += 1
            if i == len(res):
                break
            pair = res[i]
        elif idx == pair[0]:
            result += '<b>'
            result += each
        elif idx == pair[1]:
            result += each
            result += '</b>'
            i += 1
            if i == len(res):
                break
            pair = res[i]
        else:
            result += each
    if idx < len(l):
        result += ''.join(l[idx + 1: ])
    return result

print(add_bold_tag('abcxyz123', {"abc", "123"}))
print(add_bold_tag('aaabbcc', {"aaa", "aab", "bc"}))
print(add_bold_tag("aaabbcc", ["d"]))
print(add_bold_tag("aaabbcc", ["a", "b", "c"]))
print(add_bold_tag("aaabbaaa", ["aaa"]))
print(add_bold_tag("abcdef", ["a","c","e","g"])) # expected output "<b>a</b>b<b>c</b>d<b>e</b>f"
print(add_bold_tag("sgejoezpocidjlcxazelzsnialkqehztgevweghvezaaknrvyzgccxgerptvmhkmwxileecliyendyuqmphjmokzkxehztjykhtthdbmdpkpeometdhgrzedmdvnneealyzmhsddsnbwhuppwukxrdxjsqmbylenapiqmdtzzcufxhfcslatofshuetscbgpbtxsftbfrkkeeottrfiqbmgqmkypxvzemhweybvaprekbtkqugxkjpbocutdeplvnhopbmroerbzykjmczypmwuvrstbdymnlwdfnvkzdzsudgzwtxhsaalgdlwupqcsvinkdepapfvuldqklrzkhazhdipxhhfskimknwxtdsmmqbffnzgajktetdunqmvnokemdzumkysoxjmmarqahwjwkwczgzdwgvrdcrtqrgkqnhxehaccsitwnmxjjzabslmprpcebvyyonbtmjksvmtbchslrtuhrfxwleqdapzzysmqfrswhuqlfyexbqvexseyyvkhmqtqixsjwolvqkdgfwzwmcxnihhmiaxawnivdgeixewcppaormwctgdjnzyphswdnacoegydbugyscpkooaibtimfeaeyzqabhiclttzdfryvhdrocolzgdcyiedjmfrrsfoekqmkanzvxblbyqdnjluhnzzvowsmvzggnasnqkkuklcehqnlypcytrkicbqujyfsvfbnedmrgbeoksuyimrsucjrguctfhmcupcqarxqjowbkrdmaztzwmuqnxsswcvuzbmnwdawgrazvcbxmapwmaelumwivmngaqqqmxszvfpmkgpjtuabbaiskkquqhztalmomxubizmentwjsqjntlqhiivybhsombucvwuaxpevkqsqoqpmuvnizicjwheordrxbalkosogxttnbttbmfxtgxldxoqrwpvtqes", 
["sg","ej","oe","zp","oc","id","jl","cx","az","el","zs","ni","al","kq","eh","zt","ge","vw","eg","hv","ez","aa","kn","rv","yz","gc","rp","tv","mh","km","wx","il","ee","cl","iy","en","dy","uq","mp","hj","mo","kz","kx","jy","kh","tt"]))
