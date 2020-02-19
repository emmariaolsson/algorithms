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

The original algorithm does the following:
0. sort the input array
1. for every index in the input, do:
    1.1. if the past element is equal to the current element: continue
    1.2. find indexes of the next element and last element
    1.3. while we haven't gone through all elements, do:
        1.3.1. sum all indexed elements
        1.3.2. if the sum is larger than zero:
            1.3.2.1. decrease rear index
        1.3.3. else if the sum is less than zero:
            1.3.3.1. increase the front index
        1.3.4. else if the sum is zero, do:
            1.3.4.1. add the set to the result
            1.3.4.2. decrease rear index to remove duplicates
            1.3.4.2. increase front index to remove duplicates

The function can be refactored into some subfunctions
the following functions can be used:
three_sum(array):
1. sort input array
2. for every index in input, do:
    2.1. find unique sets equal to value at index
    2.2. add unique sets to output

find_unique_sets_equal_to(array, value)
1. set first and last index to front, rear
2. while front and rear index are different, do:
    2.2. if sum of front, rear is greater than value:
        2.2.1. increase front index
    2.3. else if sum i less than value:
        2.3.1. decrease rear index
    2.4. if sum is equal to value:
        2.4.1. add set to output set
        2.4.2. increase front index

After refactoring the cyclomatic complexity of the functions are:
find_unique_sets_equal_to: 4
three_sum: 2

and the total lines of code in the file has also shrunk, 
from 31 to 12 + 7 = 19 nloc

the tests also cover 100% of the code as seen by coverage.py
The main reduction of lines of code come from using the
property of sets that you canät add duplicates to them

"""

def find_unique_sets_equal_to(array, l, r, value):
    """
    :param array: list[int]
    :param l: int
    :param r: int
    :param value: int
    :return: set[ tuple[int, int, int]]
    """
    result = set()
    while l < r:
        s = value + array[l] + array[r]
        if s > 0:
            r -= 1
        elif s < 0:
            l += 1
        else:
            #result.add((100, value))
            result.add((value, array[l], array[r]))
            l += 1
    return result

def three_sum(array):
    """
    :param array: List[int]
    :return: Set[ Tuple[int, int, int] ]
    """
    result = set()
    array.sort()
    for i in range(len(array) - 2):
        s1 = find_unique_sets_equal_to(array, i + 1, len(array) -1, array[i])
        result = result.union(s1)

    return result
