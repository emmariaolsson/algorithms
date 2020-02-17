"""
   This function takes two lists and returns the node they have in common, if any.
   In this example:
   1 -> 3 -> 5
               \
                7 -> 9 -> 11
               /
   2 -> 4 -> 6
   ...we would return 7.
   Note that the node itself is the unique identifier, not the value of the node.
   """
import unittest

def intersection(h1, h2):

    count = 0
    flag = None
    h1_orig = h1
    h2_orig = h2

    visited = [0] * 15

    while h1 or h2:
        visited[0] = 1
        count += 1

        if not flag and (h1.next is None or h2.next is None):
            visited[1] = 1
            # We hit the end of one of the lists, set a flag for this
            flag = (count, h1.next, h2.next)
        else:
            visited[2] = 1

        if h1:
            visited[3] = 1
            h1 = h1.next
        else:
            visited[4] = 1

        if h2:
            visited[5] = 1
            h2 = h2.next
        else:
            visited[6] = 1

    long_len = count    # Mark the length of the longer of the two lists
    short_len = flag[0]

    if flag[1] is None:
        visited[7] = 1
        shorter = h1_orig
        longer = h2_orig
    elif flag[2] is None:
        visited[8] = 1
        shorter = h2_orig
        longer = h1_orig
    else:
        visited[9] = 1

    while longer and shorter:
        visited[10] = 1

        while long_len > short_len:
            visited[11] = 1
            # force the longer of the two lists to "catch up"
            longer = longer.next
            long_len -= 1

        if longer == shorter:
            visited[12] = 1
            # The nodes match, return the node
            print(f'Intersection coverage: {visited}')
            return longer
        else:
            visited[13] = 1
            longer = longer.next
            shorter = shorter.next
    visited[14] = 1
    return None