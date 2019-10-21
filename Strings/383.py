"""

383. Ransom Note

Given an arbitrary ransom note string and another string containing letters from all the magazines,
write a function that will return true if the ransom note can be constructed from the magazines ;
otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

"""
import collections


def ransom_note(note, available_chars):
    # using Counter
    note_count = collections.Counter(note)
    available_chars = collections.Counter(available_chars)
    for each_char in note:
        if note_count[each_char] > available_chars[each_char]:
            return False
    return True

# TC: O(n)
# SC: O(26)


ransom_note("a", "b")
ransom_note("aa", "ab")
ransom_note("aa", "aab")


def ransom_note_using_set(note, available_Chars):
    for i in set(note):
        if note.count(i) > magazine.count(i):
            # count takes O(n)
            return False
    return True


# TC: O(n^2)
