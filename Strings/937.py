"""
937. Reorder Data in Log Files

You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one
word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered
lexicographically ignoring identifier, with the identifier used in case of ties.
The digit-logs should be put in their original order.

Return the final order of the logs.

Example1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

"""

# The rules are:
#
# Letter-logs come before digit-logs;
# Letter-logs are sorted alphanumerically, by content then identifier;
# Digit-logs remain in the same order.


def reorder_log_files(logs: list) -> list:
    def custom_sort(log):
        id_, rest = log.split(" ", 1)  # only split into 2 parts
        print('Id is', id_)
        print('rest of the log - ', rest, rest[0], rest[0].isalpha())
        return (0, rest, id_) if rest[0].isalpha() else (1, )
    return sorted(logs, key=custom_sort)


reorder_log_files(["dinesh singh", "savya ananda"])

reorder_log_files(["dig1 8 1 5 1", "let1 art can", "dig2 3 6","let2 own kit dig", "let3 art zero"])
reorder_log_files(["g1 act", "a8 act aoo"])
reorder_log_files(["dig1 8 1 5 1", "dig2 3 6"])