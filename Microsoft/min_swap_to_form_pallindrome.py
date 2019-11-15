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
    for i in range(n // 2):
        found = False
        for j in range(n - i - 1, i, -1):
            if s[j] == s[i]:
                print('found')
                found = True
                for k in range(j, n - i - 1):
                    # if i = 0 and j = n => we don't need to run the k loop
                    # (abbaa) -> a at 0 and a at n match, b at 1 and a at n-1 don't match, so, when we decrement till j => we found at index 2
                    # we need to swap the elements from n-i-1 till the j index
                    s[k], s[k + 1] = s[k + 1], s[k]
                    swaps += 1
                break
    if not found and n % 2 != 0:
        # if it is not found, and the digit is odd, => "aabba" => a at index 1 can't be matched till middle. So it is definetely the odd number
        for k in range(n // 2):
            s[k], s[k + 1] = s[k + 1], s[k]
            swaps += 1

    return swaps


# print(min_swap_to_form_pallindrome("mamad"))
print(min_swap_to_form_pallindrome("ntaiain"))  # This is wrong

from collections import Counter, defaultdict


def minSwapPalindrome(S):
    # check if can swap to palindrome
    n, cnt = len(S), Counter(S)
    odd = sum(1 for k, v in cnt.items() if v % 2)
    if odd - n % 2 > 0: return -1
    # partition into left + middle (empty if n even) + right
    aux = defaultdict(list)
    for i, c in enumerate(S):
        aux[c].append(i)
    L2R, R2L, half = [], [], (n - 1) / 2
    for c, index in aux.items():
        h = cnt[c] // 2
        # for each number
        # the first h occurence must be at left
        # the last h occurence must be at right
        L2R += [i for i in index[:h] if i > half]
        R2L += [i for i in index[cnt[c] - h:] if i < half]
    # swap to make left and right anagram
    arr, size, move = list(S), n // 2, 0
    if n % 2 == 1:
        # if n odd, find the middle letter
        mid = [k for k, v in cnt.items() if v % 2][0]
        # find the index of its middle occurence
        mid_idx = aux[mid][cnt[mid] // 2]
        # if it is not at center, move it to center
        if mid_idx != size:
            move += abs(size - mid_idx)
            arr = arr[:mid_idx] + arr[mid_idx + 1:]
            arr.insert(size, mid)
            if len(L2R) < len(R2L):
                L2R = [i + (i > mid_idx) for i in L2R]
                L2R.append(mid_idx)
            else:
                R2L = [i - (i > mid_idx) for i in R2L]
                R2L.append(mid_idx)
    # swap the rest to make the array partitioned
    for i, j in zip(L2R, R2L):
        move += i - j
        arr[i], arr[j] = arr[j], arr[i]
    # s1 = left[::-1], s2 = right
    # find min swap to make s1 == s2
    s1, s2 = arr[:size][::-1], arr[-size:]
    i, swap = 0, 0
    while i < size:
        j = i
        while j < size and s1[j] != s2[i]: j += 1
        if i < j < size:
            s1[i:j + 1] = [s1[j], *s1[i: j]]
            swap += j - i
        i += 1
    return move + swap


def minSwapPalindrome1(S):
    # check if can swap to palindrome
    n, cnt = len(S), Counter(S)
    odd = sum(1 for k, v in cnt.items() if v % 2)
    if odd - n % 2 > 0: return -1
    A, ans = list(S), 0
    for i in range(n // 2):
        found = False
        for j in range(i + 1, n - i)[::-1]:
            if A[i] != A[j]: continue
            found = True
            for k in range(j, n - i - 1):
                A[k], A[k + 1] = A[k + 1], A[k]
                ans += 1
            break
        if not found and n % 2 == 1:
            for k in range(i, n // 2):
                A[k], A[k + 1] = A[k + 1], A[k]
                ans += 1
    return ans


S = 'mamad'
print(minSwapPalindrome(S))

S = 'asflkj'
print(minSwapPalindrome(S))

S = 'aabb'
print(minSwapPalindrome(S))

S = 'ntiin'
print(minSwapPalindrome(S))

S = 'frrfrra'
print(minSwapPalindrome(S))
