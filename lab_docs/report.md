# Report for assignment 3

## Project

Name:  keon/algorithms 

URL: https://github.com/keon/algorithms

Minimal and clean example implementations of data structures and algorithms in Python 3.

## Onboarding experience

Did it build and run as documented?
    
See the assignment for details; if everything works out of the box,
there is no need to write much here. If the first project(s) you picked
ended up being unsuitable, you can describe the "onboarding experience"
for each project, along with reason(s) why you changed to a different one.

We managed to build and run the project as documented. Since it is a python project, python 3 obviously had to be installed along with the following dependencies (via pip):

```
- flake8
- python-coveralls
- coverage
- nose
- pytest
- tox
- black
```

In general it was very easy to set everything up since the setup was very well documented. Furthermore, python is quite an easy language to work with.


## Complexity

1. **What are your results for ten complex functions?**
   * **Did all tools/methods get the same result?**
   
   Two of the functions did not get the same result as lizards when counted manually: `intersection` and `is_palindrome_dict`. 

   * **Are the results clear?**

   For the most part the results are clear. However, we are still unsure why `is_palindrome_dict` cyclomatic complexity is reported as 10 by lizard. See below for a guess as to why the result for `intersection` differs.

**Lizard CCN**

| NLOC     | CCN     | NAME                                                                        |
|------    |-----    |-------------------------------------------------------------------------    |
| 50       | 20      | strip_url_params1@14-68@./algorithms/strings/strip_url_params.py            |
| 49       | 18      | delete_fixup@209-269@./algorithms/tree/red_black_tree/red_black_tree.py     |
| 46       | 13      | text_justification@34-89@./algorithms/strings/text_justification.py         |
| 35       | 11      | fix_insert@88-141@./algorithms/tree/red_black_tree/red_black_tree.py        |
| 33       | 12      | edmonds_karp@43-80@./algorithms/graph/maximum_flow.py                       |
| 31       | 14      | intersection@21-64@./algorithms/linkedlist/intersection.py                  |
| 30       | 10      | maximum_flow_dfs@27-83@./algorithms/graph/maximum_flow_dfs.py               |
| 27       | 10      | maximum_flow_bfs@28-84@./algorithms/graph/maximum_flow_bfs.py               |
| 26       | 13      | bracket@69-95@./algorithms/strings/breaking_bad.py                          |
| 26       | 10      | is_palindrome_dict@52-89@./algorithms/linkedlist/is_palindrome.py           |

**Manually counted CCN**

- *is_palindrome_dict@52-89@./algorithms/linkedlist/is_palindrome.py*

   The cyclomatic complexity of the function is 10 according to lizard. However, with McCabe's, where π = 9 and s = 4 we get complexity 7. The complexity is reduced a lot because of the many return statements throughout the function, could this be why the results from manual counting differs?

- *edmonds_karp@43-80@./algorithms/graph/maximum_flow.py*

   The cyclomatic complexity of the function is 12. The same value was calculated using Mccabe’s formula with π = 11 and s = 1.

- *intersection@21-64@./algorithms/linkedlist/intersection.py*

   The cyclomatic complexity of the function is 14 according to lizard. By using McCabe’s formula we count a cyclomatic complexity of 13, where π = 13, s = 2. The reason for this could be that the function returns `None` at the end if no merge is found. This isn't really necessary because not returning anything in Python also returns `None` and would give use the same complexity as lizard.

- *fix_insert@88-141@./algorithms/tree/red_black_tree/red_black_tree.py*

    The cyclomatic complexity according to lizard is 11. Using McCabe’s formula we get with π = 10, s = 1: M = 10-1+2= 11

- *delete_fixup@209-269@./algorithms/tree/red_black_tree/red_black_tree.py*

    The cyclomatic complexity of the function is 18. Using McCabe’s formula with π = 16 and s = 0 we also get 18.

2. **Are the functions just complex, or also long?**

   Longer functions usually are more complex in the project. However, there are cases where NLOC is lower but the complexity higher.

3. **What is the purpose of the functions?**

- *strip_url_params1@14-68@./algorithms/strings/strip_url_params.py*

    Removes any duplicate query string parameters from the url, and any query string parameters specified within the 2nd argument. This function requires a high CC since it goes through several paths to find out what to add to the resulting string (URL). The complexity is more or less necessary. The function is very long since it checks each parameters length, if it has been added to the resulting url, if it must be removed, etc.

- *delete_fixup@209-269@./algorithms/tree/red_black_tree/red_black_tree.py*

    When deleting a node the color of the red black tree also needs to be updated. Just like when fixing insert we also need to go over the graph and color the graph differently depending on the color of the removed node and its relatives which gives us by necessity a high CC. When "fixing" the graph there are many different cases to consider which also increases the complexity.

- *is_palindrome_dict@52-89@./algorithms/linkedlist/is_palindrome.py*

    The function determines if a linked list is a palindrome. It does this by constructing a dictionary where the keys are the values of the list, and the values are the positions at which these values occur in the list. It determines if the linked list is a palindrome by iterating the dictionary and making sure certain criteria are met. The cylcomatic complexity is high and has to be because the function first places the linked list into a dictionary. Thereafter, it iterates the dictionary to figure out if it is a palindrome. 

- *text_justification@34-89@./algorithms/strings/text_justification.py*

    Justifies a text by padding the spaces between words with extra spaces in order to fill out the words to fit a certain given width. This function has a high CC because of the couple of different cases that have different approaches defined. 

- *edmonds_karp@43-80@./algorithms/graph/maximum_flow.py*

    The function computes the maximum flow between source and sink in a graph using BFS. This requires a high CC since it needs to search through the graph and many branches are possible.

- *intersection@21-64@./algorithms/linkedlist/intersection.py*

    The purpose of the intersection method is to find the node where two linked lists merge into one. This is often used to check for errors because it is most likely unwanted behaviour/functionality. The cyclomatic complexity is high because the function first has to figure out which of the lists is the longer and shorter one with the help of a while loop. Personally, I feel like this method is unecessarily complex for what it does.

- *maximum_flow_bfs@28-84@./algorithms/graph/maximum_flow_bfs.py*

    Given a n*n adjacency matrix this function will return the maximum flow, using BFS to find the path consisting of maximum weights. This requires high CC since all nodes are stored in a queue and an array, while the path is stored in its own data structure. 

- *maximum_flow_bfs@28-84@./algorithms/graph/maximum_flow_dfs.py*

    Given a n*n adjacency array this function will return the maximum flow. This version uses DFS to find an augmented path. This requires a high CC because the function runs the bfs of the residual graph multiple times.

- *bracket@69-95@./algorithms/strings/breaking_bad.py*

    The breaking bad function takes an array of words and an array of symbols and displays the word(s) with their matched symbol surrounded by square brackets

    ```
    Example:
    Words array: ['Amazon', 'Microsoft', 'Google']
    Symbols: ['i', 'Am', 'cro', 'Na', 'le', 'abc']
    Output:
    [Am]azon, Mi[cro]soft, Goog[le]
    ```

    The complexity of this function should be high because the program to iterate multiple word lists and characters inside those words. It is further increased by storing the symbols in a dictionary before using them. 

- *fix_insert@88-141@./algorithms/tree/red_black_tree/red_black_tree.py*

    When inserting a node into a red-black tree the color of the tree needs to be updated to work with the new node according to the rules of coloring a red-black tree. This means that we need to look at the color of the relatives of the inserted node to figure out how we should recolor the graph. Depending on the current colors of the relatives we therefore take different paths and a high CC is required.

- *three_sum@18-48@./algorithms/array/three_sum.py*

   Gives all unique sets of three distinct integers from a list that sum to zero. Has high complexity because of the way the function deals with duplicate sets

- *knuth_morris_pratt@10-34@./algorithms/strings/knuth_morris_pratt.py*

   Given a text string and a pattern string, this function will find all the start indexes in the text that matches with the pattern using knuth_morris_pratt algorithm. In other words: where in the text the pattern string can be found.


- *valid_solution_hashtable@10-37@./algorithms/matrix/sudoku_validator.py*

   Determines whether a given 9x9 matrix is a valid sudoku solution or not. It has high complexity due to stored information of the cells and that it compares value to the rest if the row and column. 

4. **Are exceptions taken into account in the given measurements?**

   Python uses exceptions and they are taken into account by the tool. This was tested by measuring the CC for a method that only had a single return and comparing it with a method that had a `try/catch` and a return. The test showed that the `try/catch` increases the CC by one.

5. **Is the documentation clear w.r.t. all the possible outcomes?**

   Some of the functions are very well documented. For example, the linked list intersection function clearly describes how it works and when it returns true or false. However, the documentation is not as good for most of the functions. In these cases, the programmer reading the code has to figure out the possible outcomes induced by the branching. 


## Coverage

### Tools

We used `coverage.py` to measure the branch coverage. The tool was very easy to use since it works with many testing environments in python, including `pytest` which is used in the project. 

The tool is very well documented, clearly explaining how to install it and run it with the different testing environments: 

https://coverage.readthedocs.io/en/coverage-5.0.3/


### DYI

Branch coverage was measured by creating a list of integers at the beginning of the function. Afterwards, when a branch was accessed a `1` was placed in the list at the corresponding index of that specific branch. At the end of the function or before a return, the list was printed, subsequently showing the branch coverage. If there are multiple tests for a single function you would have to “OR” the list of booleans together and calculate the coverage from the resulting list, see below.

```
[1, 0] OR [0, 1] -> [1, 1] which means 100% coverage
```

**Patch**:

For example:
`git diff 7c4998f3a80708d1eff1a2694ad3e71dc5ca56f2` 

Note that in this patch the `intersection` test was located in the program code file. It had to be moved into the test folder in order for the test to be run and the branch coverage measured.

**What kinds of constructs does your tool support, and how accurate is its output?**

The output of the tool is as accurate as the programmer makes it out to be. Since the user has to manually add lines of array assignments there is a risk that a branch is missed thus making it less accurate. Our tool did also not always get the same branch coverage percentage as `coverage.py`.

### Evaluation

1. **How detailed is your coverage measurement?**

   The coverage measurement, if implemented correctly should cover every branch and give accurate results. However, the results are simply printed as integer lists and in that sense not very detailed.

2. **What are the limitations of your own tool?**

   The limitations of the tool are obvious. Firstly, the tool alters the source code since the list of visited branches has to be updated. Secondly, this also means that if the source code changes, the branch coverage code would have to be rewritten. Furthermore, the results presented by the tool are basic, it just prints out the list. This means that the programmer has to calculate the branch coverage percentage manually which can be tedious if there are many branches and tests. 

3. **Are the results of your tool consistent with existing coverage tools?**

   As mentioned before, it does not always get the same branch coverage percentage as `coverage.py`. It was sometimes hard to compare though because `coverage.py` calculates the coverage for the whole file, not individual functions.

### Coverage improvement

Below is a list of each function. It describes the current tests and new requirements that have to be tested in order to increase or achieve 100% branch coverage. Additionally, a patch is included if all or some of the requirements have been tested with new tests.

- *intersection@21-64@./algorithms/linkedlist/intersection.py*

   There is only one test for this function which results in a branch coverage of ~66%. The test calls the function with two linked lists of the same length who merge together into a single linked list.

   The test does not try to call the method with two linked lists who do not merge, i.e. two separate linked lists. Additionally, a crucial while loop used when one of the lists is longer than the other is never tested. 

   New requirments:

   * Requirement 1: Call the function with two linked lists who do not merge. Expect `None` object to be returned since no common node should be found.
   
   * Requirement 2: Call the function with two linked lists that merge, where one of the lists is significantly longer. Expect to get the element in common (where they merge). This tests one crucial loop in the function that was not tested before.

   Patch: `git diff b53a90b564cc4ec337d9cc5172a6edca798391e3 tests/test_linkedlist.py`

- *bracket@69-95@./algorithms/strings/breaking_bad.py*

   There is only one test for the breaking_bad bracket function. It tests an arbitrary input  with three words and three input symbols where a match is found in each word. The tests do not cover cases where, for example, there is no match or where a symbol is mentioned twice in the input (e.g. `[i,i]` could result in a double encapsulation `[[i]]` which is not desired).

   New requirements:

   * Requirement 1: Call the function with symbols that do not match any of the supplied words. Expect to get the original words as a tuple with no changes to them. 

   * Requirement 2: Call the function with two identical symbols in order to get full branch coverage. Expect the symbols to only be swapped once and not end up in a situation where the symbol is surrounded by two brackets, e.g. `M[[i]]crosoft` if the symbols are `[i, i]`.

   Patch: `git diff 3c1c5dfaac0e252bb7d456c78343537a1915acd5 tests/test_strings.py`

- *fix_insert@88-141@./algorithms/tree/red_black_tree/red_black_tree.py*

   No tests exist for any of the red black tree functions and therefore we get a branch coverage of 0%.

   New requirements:

   * Requirement 1: Null parent should set inserted node as root and color to black

   * Requirement 2: The parent color is black, then nothing should be done and function should return.

   * Requirement 3: Parent is left of grandparent, parent color and uncle color is red, then set parent and uncle color to black and grandparent to red. Set this node equal to parent node

   * Requirement 4: Parent is left of grandparent, uncle is black or null and the node is right of parent, then set this node equal to parent node and rotate node to the left

   * Requirement 5: Parent is left of grandparent,  uncle is black and node is left of parent, set parent color to black, grandparent to red and rotate grandparent right

   * Requirement 6: Parent is right of grandparent & uncle is red, then set parent and uncle to black and grandparent to red and set node equal to parent.

   * Requirement 7: Parent is right of grandparent, uncle is black or null and node is right of parent, then set node equal to parent and rotate node right.

   * Requirement 8: Parent is right of grandparent & uncle is black, then set parent color to black, grandparent to red and left rotate grandparent.

   Patch: `git diff 6002a49b1ffc4eaaccae15650ac460e9dca132e7 tests/test_tree.py`

- *is_palindrome_dict@52-89@./algorithms/linkedlist/is_palindrome.py*

   For this function there are two assertion tests, consisting of one valid test case and one invalid test case. The branch coverage was 75%. 

   New requirements:

   * Requirement 1: If the linked list is empty, meaning there is no “head”, it is still considered a palindrome and the function should return True.

   * Requirement 2: If the linked list consists of a single node, it is still considered a palindrome and the function should return True.

   * Requirement 3: If the number of nodes in the linked list is even and the first half is the equivalent to the second half backwards, it should return True.

   * Requirement 4: If the number of nodes in the linked list is odd and the elements from index 0 to (length-1)/2, correspond with the elements from length-1, tracing backwards to (length+1)/2 the function should return True.

   Patch: `todo`

- *valid_solution_hashtable@10-37@./algorithms/matrix/sudoku_validator.py*

   There are two tests for this function, one assertTrue with a valid solution and one assertFalse with multiple zeroes spread out in the matrix (value 0 means empty cell and should return False).

   New requirements:

   * Requirement 1: There must be integers in each cell of the matrix. A matrix containing any cells with None values should return False.

   * Requirement 2: The value in each cell is supposed to be in the range 1 to 9. A matrix containing any cells with value 0 should return False.

   * Requirement 3: The value in each cell cannot have a duplicate on the same row. If there are two or more of the same value on the same eow, the function should return False.

   * Requirement 4: The value in each cell cannot have a duplicate in the same column. If there are two or more of the same value in the same column, the function should return False.

   * Requirement 5: The values on one row must add up to 45 for the function to return True.

   Patch: `todo`

- *strip_url_params1@14-68@./algorithms/strings/strip_url_params.py*

   The test suite contains 2 tests, which results in a branch coverage of 85%. Test 1 calls the function with a URL containing 3 parameters (a=1, b=2, a=2), where 2 of them have the same key. The test checks that the same parameter is not used more than one time. Test 2 calls the function with a URL containing 2 parameters (a=1 & b=2) and the parameter to be removed (b). This function checks that the assigned parameter is removed from the url.

   There is no test that handles the case where the function is called with a parameter (to be removed from the url) and a url with parameters, where the parameter to be removed appears first.

   No test covers the case where the function is called with a url without parameters.

   There is no test that handles the case where the function is called with a url containing a parameter without a key, ex: kth.se?=3. In this case the function should still return a valid url, ex: kth.se  

   New requirements:

   * Requirement 1: Call the function with a url with parameters (where the first is the one to be removed) and a parameter that is going to be removed. The same url must be  returned, but without the parameter that is going to be removed.

   * Requirement 2: Call the function with a url not containing any parameters. The same url must be returned.

   * Requirement 3: Call the function with a url containing a parameter without a key. The  same url must be returned, but without the parameter. 
   
   Patch: `git diff 1d328293f3e03cced13f8e95495cfda1627a2730 tests/test_strings.py`

- *knuth_morris_pratt@10-34@./algorithms/strings/knuth_morris_pratt.py*

   The testsuite contains 3 tests, which results in 95% branch coverage. What’s common for all tests is that the function is called with a text string and a pattern string. Test 1 checks that the correct list of indexes is returned when searching for the start indexes in the text string that matches with the pattern. In this case all text characters are equal to the pattern characters (which consists of the same character). The purpose of test 2 is the same, but this time the pattern characters are not the same, and the text characters are not the same as the pattern characters. Test 3 is expecting an empty list to be returned since the pattern string can’t be found in the text string.

   There is no test that calls the function with a pattern string with it’s first two characters being the same, and that the correct list of indexes is returned.

   New requirements:

   * Requirement 1: Call the function with a pattern string where the first two characters are the same. The function is expected to still return the correct list of indexes.

   Patch: `git diff 6afcc9dca4a274b133e9d01684d9282282b9ee21 tests/test_strings.py`
   
- *text_justification@34-89@./algorithms/strings/text_justification.py*
   
   There are two test sets for this function that test that the given inputs give som given outputs. They both test some regular cases but only some of the edge cases for the functions. They do not test that a word that is exactly as long as the line width is written on one line for example.
   
   New rquirements:
   
   * The function must output a list of strings of length max_width which is given as an input
   * The function must throw a value error if a word in the input is longer than max_width
   * The function must separate each word with at least one blank space or a line break
   * The function must add trailing spaces in order to fit a word to a line if the next word does not fit to the line
   
   Patch: `git diff f6fc4bba2a6d1b296e9d51dbafa5c756bf3f4596 tests/test_strings.py`


- *three_sum@18-48@./algorithms/array/three_sum.py*
   
   There are two test sets for this function that test that given inputs give some given outputs. This tests that the function gives sets of solutions with three integers each. 
   
   New rquirements:
   
   * All arrays in the output set must be unique with regards to the output set
   * All arrays returned must be of length three
   * All arrays returned must sum to zero
   * All arrays returned must contain values that exist in the input set
   * Entries in the output arrays must be unique and distinct from the input set
   
   Patch: `git diff 2331357ab76a00cc78f57b15f171f10fa56ce236 tests/test_array.py`

TODO: add htmlcov files to git? and link index.html before and after?

Report of old coverage: https://github.com/emmariaolsson/algorithms 

Report of new coverage: https://github.com/emmariaolsson/algorithms/tree/assessment-tests

## Refactoring

The plan for refactoring complex code was mostly to split up the functions into several separate ones. This lowers the CC but can in some cases have some drawbacks in the form of too many, very specialised functions. Below is the plan for every refactor.

- *is_palindrome_dict@52-89@./algorithms/linkedlist/is_palindrome.py*

   The cyclomatic complexity of this function was 10 to begin with and is necessary in the sense that all complex iterations are needed to determine if the input is valid or not. However, the cyclomatic complexity could be significantly decreased by extracting helpfunctions. The function consists of a while-loop in which the dictionary is filled depending on an if-statement. The while-loop is then followed by a for-loop containing an if-statement which checks if the values appear an even number of times. If not, it iterates over the the values that are repeated and determine if they have the corresponding positions forwards and backwards. By extracting three helpfunctions (fill_dict with the while-loop, check_valid_palindrome with the outer for-loop and even_palindrome with the inner for-loop) the cyclomatic complexity was decreased with 50%, from 10 to 5.

   Patch: `todo`

- *edmonds_karp@43-80@./algorithms/graph/maximum_flow.py*

   The cyclomatic complexity of the function is 12. The complexity is required to calculate the flow since we need to search through the graph and we have no option but to have a few loops to do this. We can however reduce the cyclomatic complexity splitting the function into smaller units. It exists a while loop that contains a for loop that finds the new flow using BFS, these could be moved to two separate functions. There also exists a while loop that updates the flow array that could also be moved to a third function. This halves the cyclomatic complexity from 12 to 6.

   Patch: `git diff 920cc6bcdb8b6b55c22bda09adb48ce20776a027  algorithms/graph/maximum_flow.py`

- *intersection@21-64@./algorithms/linkedlist/intersection.py*

   The cyclomatic complexity of the function is 14 and is more or less necessary to be that high. The function is very long since it first has to iterate the linked lists to find which of the two lists are longer. Thereafter, it tries to find a common node where they merge. Since these are two different distinct functionalities, they can be separated into two different functions and subsequently reduce the cyclomatic complexity of the original function. This should lower the complexity since the more complex part of finding information about the lists is moved into another function. 
   
   Patch: `git diff 362556e10902e900d476ffe13fc9c36e07683c8d algorithms/linkedlist/intersection.py`

- *bracket@69-95@./algorithms/strings/breaking_bad.py*

   The cyclomatic complexity of the function is 13. The function is complex because it has to iterate two lists of words and in those list items iterate characters. The cycomatic complexity can be reduced by splitting the function into three separate functions. More specifically, one function for adding symbols to a dictionary, one for the while loop executed on each word and one for the original function that calls the other two. 

   Patch: `git diff 6d5cccc1741ef961286542cb433de9e705978b1e algorithms/strings/breaking_bad.py`

- *fix_insert@88-141@./algorithms/tree/red_black_tree/red_black_tree.py*

   The cyclomatic complexity of fix_insert is 11. The high complexity of fix insert is required. In fix insert we need to recolor and or rebalance the tree to follow the red black tree standards after an insert. The red black trees rules about how the tree should be colored and balanced therefore require us to have many different cases to consider. It is however possible to split the function up in multiple smaller units to reduce the complexity. Specifically we could move the code where parent is left of grandparent, and parent is right of grandparent to other functions. This should reduce the complexity with 4 and result in a cyclomatic complexity of 7 which is a decrease of approximately 36 %.

   Patch: `git diff 3ce4ad072d14d2103f5645078cc321bff70a3350 algorithms/tree/red_black_tree/red_black_tree.py`


-  *strip_url_params1@14-68@./algorithms/strings/strip_url_params.py*

   The cyclomatic complexity of this function is 20. The complexity is more or less necessary. The function is very long since it checks each parameters length, if it has been added to the resulting url, if it must be removed, etc. It’s possible to reduce this complexity by dividing the code into smaller units. The part of the code that is responsible for checking whether a parameter should be added to the final url (to be returned by the function) can have its own function. Doing this reduces the complexity from 20 to 7 (65% reduction).

   Patch: `git diff 2c3122e9f126959927fc8b24ea46c1354833ce22 algorithms/strings/strip_url_params.py`

- *maximum_flow_dfs@27-83@./algorithms/graph/maximum_flow_dfs.py*

   The cyclomatic complexity of this function is 10. The complexity is necessary because the functionality of the function requires the program to use the dfs algorithms to find a path, get the minimum flow and reduce the capacity. It’s possible to reduce this complexity by dividing the function inte smaller units. The bfs algorithm now has its own function, and so does the part of the code that reduces the capacity. These changes reduces the complexity from 10 to 3 (70% reduction)

   Patch: `git diff 43f9add34b0ef402ae3c84c07b29b5a7cc6d64d9 algorithms/graph/maximum_flow_dfs.py`

- *valid_solution_hashtable@10-37@./algorithms/matrix/sudoku_validator.py*

   The initial cyclomatic complexity of this function was 12. The complexity was necessary since the problem of sudoku relies on stored history from previous iterations when validating the matrix values. By moving out two of the for-loops into two separate helpfunctions check_valid_value and check_addition, the complexity was decreased from 12 to 3 (75% reduction). 

   Patch: `todo`
   
- *text_justification@34-89@./algorithms/strings/text_justification.py*
   
   This function has a high cyclomatic complexity because of the many cases it has to take into account when justifying text to a given line width. This can be reduced by splitting the function into several different functions that each have their own functional requirements. The text_justification function can be split up into a left_align and fit_words_to_row function that takes a list of words in an input and add trailing spaces or padding spaces between these words respectively. One can also move the counting of what words fit in the next row into a separate function, this would massively decrease the cyclomatic complexity and make testing easier. 
   
   Patch: `git diff c9c1440972dc27e3b88810eea5e82d244cfad1fc algorithms/strings/text_justification.py`


- *three_sum@18-48@./algorithms/array/three_sum.py*
   
   The original function has high cyclomatic complexity mainly because of the way it handles duplicates in the function. One can instead use the property of python sets that state that there can be no duplicates in the set which basically means that the three_sum function does not need to handle duplicate cases. It is also possible to reduce complexity by adding a helper function that replaces part of the function into a separate function. This function would check for pairs in the input array which sum to a given value, this will reduce the cyclomatic complexity of the three_sum function.
   
   Patch: `git diff aac4618c43d9e79bcfb1164b2119ef70f6cdfbf4 algorithms/array/three_sum.py`


## Overall experience

**What are your main take-aways from this project? What did you learn?**

We learnt a lot about branch coverage and cylcomatic complexity. It was also interesting to work on an open source project even though the one we selected wasn't that complicated to build and run. 


