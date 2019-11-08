"""
Alexa is given n piles of equal or unequal heights. In one step, Alexa can remove any number of boxes from the pile which has the maximum height and try to make it equal to the one which is just lower than the maximum height of the stack. Determine the minimum number of steps required to make all of the piles equal in height.

Example 1:

Input: piles = [5, 2, 1]
Output: 3
Explanation:
Step 1: reducing 5 -> 2 [2, 2, 1]
Step 2: reducing 2 -> 1 [2, 1, 1]
Step 3: reducing 2 -> 1 [1, 1, 1]
So final number of steps required is 3.
"""

def min_steps_to_make_piles_equal(piles):
    # does it contain duplicates ?? yes
    piles.sort(reverse=True)
    start = 0
    end = 0
    count = 0
    while end < len(piles):
        # 5, 5, 2, 2, 1
        if piles[start] == piles[end]:
            end += 1 # find for a better sol
        else:
            # when they are not equal make piles[start] = piles[end] and increment start till start == end
            while start <= end:
                if piles[start] != piles[end]:
                    piles[start] = piles[end]
                    print(piles)
                    count += 1
                start += 1
            start = 0
            end += 1
    return count

print(min_steps_to_make_piles_equal([5, 2, 1]))
print(min_steps_to_make_piles_equal([7, 7, 4, 7, 1]))
