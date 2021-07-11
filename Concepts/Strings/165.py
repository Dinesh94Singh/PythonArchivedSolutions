"""
165. Compare Version Numbers

Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.

The . character does not represent a decimal point and is used to separate number sequences.

For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the
second first-level revision.

You may assume the default revision number for each level of a version number to be 0. For example, version number 3.4
has a revision number of 3 and 4 for its first and second level revision number.
Its third and fourth level revision number are both 0.



Example 1:

Input: version1 = "0.1", version2 = "1.1"
Output: -1
Example 2:

Input: version1 = "1.0.1", version2 = "1"
Output: 1
Example 3:

Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1
Example 4:

Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation: Ignoring leading zeroes, both “01” and “001" represent the same number “1”
Example 5:

Input: version1 = "1.0", version2 = "1.0.0"
Output: 0
Explanation: The first version number does not have a third level revision number, which means its third level revision
number is default to "0"


Note:

Version strings are composed of numeric strings separated by dots . and this numeric strings may have leading zeroes.
Version strings do not start or end with dots, and they will not be two consecutive dots.


"""



def compareVersion(v1, v2):
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


# compare_versions('0.1', '1.1')
# compare_versions('0.4', '1.7')
# compare_versions('1.7', '0.4')
# compare_versions('7.5.2.3', '7.5.3')
# compare_versions('7.5.2', '7.5.2.6')
# compare_versions('1.01', '1.001')
# compare_versions('1.0.0', '1.0')
# print(compareVersion("1", "1.1"))
print(compareVersion("1.0", "1"))