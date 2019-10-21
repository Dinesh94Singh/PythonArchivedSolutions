"""

Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.

 
Follow up:
Could you solve it using only O(1) extra space?

 
Example 1:

Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
 

Example 2:

Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.
 

Example 3:

Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.
 
"""


def compress(chars):
    anchor = write = 0
    for read, c in enumerate(chars):
        if read + 1 == len(chars) or chars[read + 1] != c:
            chars[write] = chars[anchor]
            write += 1
            if read > anchor:
                for digit in str(read - anchor + 1):
                    chars[write] = digit
                    write += 1
            anchor = read + 1
    print(chars)
    return write


def my_compress(chars):
    pos = 0
    i, count = 0, 0
    while i < len(chars) - 1:
        if chars[i] != chars[i + 1] or i == len(chars) - 2:
            chars[pos] = chars[i]
            pos += 1
            count += 1
            """ can't use count - because it would be extra space. Given constraint - do it without extra space. """
            if count > 1:
                for digit in str(count):
                    chars[pos] = digit
                    pos += 1
            count = 0
        else:
            count += 1
        i += 1
    return chars


print(compress(["a", "b", "b", "b"]))
print(compress(["a", "a", "b", "b", "c", "c", "c"]))

print(my_compress(["a", "b", "b", "b"]))
print(my_compress(["a", "a", "b", "b", "c", "c", "c"]))
print(my_compress(["a", "a", "b", "b", "c", "c", "c", "c"]))

