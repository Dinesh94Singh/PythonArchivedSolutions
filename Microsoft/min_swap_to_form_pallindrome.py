"""
Given a string, what is the minimum number of adjacent swaps required to convert a string into a palindrome. If not possible, return -1.

Input: "mamad"
Output: 3
Example 2:

Input: "asflkj"
Output: -1
Example 3:

Input: "aabb"
Output: 2
Example 4:

Input: "ntiin"
Output: 1
Explanation: swap 't' with 'i' => "nitin"
"""
from collections import Counter
def min_swap_to_form_pallindrome(s):
    def canPermutePalindrome(s):
        c = Counter(s)
        limit = True
        for key in c.keys():
            value = c[key]
            if value % 2 == 0:
                pass
            else:
                if limit:
                    limit = False
                else:
                    return False
        return True

    if not canPermutePalindrome(s):
        return -1

    swaps = 0
    s = list(s)
    n = len(s)
    # compare (0, n) -> (1, n-1) -> (2, n-2) => when they don't match,
    # find the index where the same element is there. We for sure know its there, because we checked if palindrome can be formed or not.
    for i in range(n//2):
        found = False
        for j in range(n - i - 1, i, -1):
            if s[j] == s[i]:
                print('found')
                found = True
                for k in range(j, n-i-1):
                    # if i = 0 and j = n => we don't need to run the k loop
                    # (abbaa) -> a at 0 and a at n match, b at 1 and a at n-1 don't match, so, when we decrement till j => we found at index 2
                    # we need to swap the elements from n-i-1 till the j index
                    s[k], s[k+1] = s[k+1], s[k]
                    swaps += 1
                break
    if not found and n % 2 != 0:
        # if it is not found, and the digit is odd, => "aabba" => a at index 1 can't be matched till middle. So it is definetely the odd number
        for k in range(n//2):
            s[k], s[k + 1] = s[k+1], s[k]
            swaps += 1

    return swaps

# print(min_swap_to_form_pallindrome("mamad"))
print(min_swap_to_form_pallindrome("ntaiain")) # This is wrong
