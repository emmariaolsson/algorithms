"""
Given an array S of n integers, are there three distinct elements
a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
{
  (-1, 0, 1),
  (-1, -1, 2)
}
"""

"""
The cyclopmatic complexity as calculated by lizard is
11 and the lines of code is 31. 

The function have the following requirements:

1. any array returned can't be equal to another array
2. all arrays returned must have the length three
3. all arrays returned must sum to 0 (zero)
4. all arrays must contain entries that exist in input
5. entries in the arrays must be unique entries from 
    the input set

The current tests cover 95% of code according to 
coverage.py

The current coverage using the ad-hoc tool adds upp to
8 out of 9 branches

The current tests cover the following requirements:
[1, 2, 3, 4, 5]
But not in robust ways and not in several different ways



"""


def three_sum(array):
    """
    :param array: List[int]
    :return: Set[ Tuple[int, int, int] ]
    """
    visited = [0] * 9
    res = set()
    array.sort()
    for i in range(len(array) - 2):
        visited[0] += 1
        if i > 0 and array[i] == array[i - 1]:
            visited[1] += 1
            continue
        else:
            visited[2] += 1
        l, r = i + 1, len(array) - 1
        while l < r:
            visited[3] += 1
            s = array[i] + array[l] + array[r]
            if s > 0:
                visited[4] += 1
                r -= 1
            elif s < 0:
                visited[5] += 1
                l += 1
            else:
                visited[6] += 1
                # found three sum
                res.add((array[i], array[l], array[r]))

                # remove duplicates
                while l < r and array[l] == array[l + 1]:
                    visited[7] += 1
                    l += 1

                while l < r and array[r] == array[r - 1]:
                    visited[8] += 1
                    r -= 1

                l += 1
                r -= 1
    print(visited)
    return res
