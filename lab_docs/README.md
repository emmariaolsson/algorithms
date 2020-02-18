# Grading criteria

## You identify ten functions/methods with high complexity, and document the purpose of them, and why the complexity should be high (or not)

### Functions

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

### Purpose and complexity 

- **strip_url_params1@14-68@./algorithms/strings/strip_url_params.py**

    Removes any duplicate query string parameters from the url, and any query string parameters specified within the 2nd argument. This function requires a high CC since it goes through several paths to find out what to add to the resulting string (URL). The complexity is more or less necessary. The function is very long since it checks each parameters length, if it has been added to the resulting url, if it must be removed, etc.

- **delete_fixup@209-269@./algorithms/tree/red_black_tree/red_black_tree.py**

    When deleting a node the color of the red black tree also needs to be updated. Just like when fixing insert we also need to go over the graph and color the graph differently depending on the color of the removed node and its relatives which gives us by necessity a high CC. When "fixing" the graph there are many different cases to consider which also increases the complexity.

- **is_palindrome_dict@52-89@./algorithms/linkedlist/is_palindrome.py**
    
    The function determines if a linked list is a palindrome. It does this by constructing a dictionary where the keys are the values of the list, and the values are the positions at which these values occur in the list. It determines if the linked list is a palindrome by iterating the dictionary and making sure certain criteria are met. The cylcomatic complexity is high and has to be because the function first places the linked list into a dictionary. Thereafter, it iterates the dictionary to figure out if it is a palindrome. 

- **text_justification@34-89@./algorithms/strings/text_justification.py**

    TODO!!!! 


- **edmonds_karp@43-80@./algorithms/graph/maximum_flow.py**

    The function computes the maximum flow between source and sink in a graph using BFS. This requires a high CC since it needs to search through the graph and many branches are possible.

- **intersection@21-64@./algorithms/linkedlist/intersection.py**

    The purpose of the intersection method is to find the node where two linked lists merge into one. This is often used to check for errors because it is most likely unwanted behaviour/functionality. The cyclomatic complexity is high because the function first has to figure out which of the lists is the longer and shorter one with the help of a while loop. Personally, I feel like this method is unecessarily complex for what it does.

- **maximum_flow_bfs@28-84@./algorithms/graph/maximum_flow_bfs.py**

    Given a n*n adjacency matrix this function will return the maximum flow, using BFS to find the path consisting of maximum weights. This requires high CC since all nodes are stored in a queue and an array, while the path is stored in its own data structure. 

- **maximum_flow_bfs@28-84@./algorithms/graph/maximum_flow_dfs.py**

    Given a n*n adjacency array this function will return the maximum flow. This version uses DFS to find an augmented path. This requires a high CC because the function runs the bfs of the residual graph multiple times.

- **bracket@69-95@./algorithms/strings/breaking_bad.py**
    
    The breaking bad function takes an array of words and an array of symbols and displays the word(s) with their matched symbol surrounded by square brackets

    ```
    Example:
    Words array: ['Amazon', 'Microsoft', 'Google']
    Symbols: ['i', 'Am', 'cro', 'Na', 'le', 'abc']

    Output:
    [Am]azon, Mi[cro]soft, Goog[le]
    ```

    The complexity of this function should be high because the program to iterate multiple word lists and characters inside those words. It is further increased by storing the symbols in a dictionary before using them. 

- **fix_insert@88-141@./algorithms/tree/red_black_tree/red_black_tree.py**

    When inserting a node into a red-black tree the color of the tree needs to be updated to work with the new node according to the rules of coloring a red-black tree. This means that we need to look at the color of the relatives of the inserted node to figure out how we should recolor the graph. Depending on the current colors of the relatives we therefore take different paths and a high CC is required.

## You manually count the complexity of five functions (on paper or as comments)

For the manually calculation of the cyclomatic complexity, McCabe’s formula M = π - s + 2 was used (π = # decisions and s = # endpoints). We also confirmed with additional control flow graphs. 

- **is_palindrome_dict@52-89@./algorithms/linkedlist/is_palindrome.py**

    The cyclomatic complexity of the function is 10 according to lizard. However, with McCabe's, where π = 9 and s = 4 we get complexity 7. The complexity is reduced a lot because of the many return statements throughout the function.

- **edmonds_karp@43-80@./algorithms/graph/maximum_flow.py**

    The cyclomatic complexity of the function is 12. The same value was calculated using Mccabe’s formula with π = 11 and s = 1.

- **intersection@21-64@./algorithms/linkedlist/intersection.py**

    The cyclomatic complexity of the function is 14 according to lizard. However, by using McCabe’s formula we count a cyclomatic complexity of 13, where π = 13, s = 2. The reason for this could be that the function returns `None` at the end if no merge is found. This isn't really necessary because not returning anything in Python also returns `None` and would give use the same complexity.

- **fix_insert@88-141@./algorithms/tree/red_black_tree/red_black_tree.py**

    The cyclomatic complexity according to lizard is 11. Using McCabe’s formula we get with π = 10, s = 1: M = 10-1+2= 11

- **delete_fixup@209-269@./algorithms/tree/red_black_tree/red_black_tree.py**

    The cyclomatic complexity of the function is 18. Using McCabe’s formula with π = 16 and s = 0 we also get 18.

## You clearly describe how to refactor five (we did 10) complex functions into smaller functions.

- **is_palindrome_dict@52-89@./algorithms/linkedlist/is_palindrome.py**

    The cyclomatic complexity of this function was 10 to begin with and is necessary in the sense that all complex iterations are needed to determine if the input is valid or not. However, the cyclomatic complexity could be significantly decreased by extracting helpfunctions. The function consists of a while-loop in which the dictionary is filled depending on an if-statement. The while-loop is then followed by a for-loop containing an if-statement which checks if the values appear an even number of times. If not, it iterates over the the values that are repeated and determine if they have the corresponding positions forwards and backwards. By extracting three helpfunctions (fill_dict with the while-loop, check_valid_palindrome with the outer for-loop and even_palindrome with the inner for-loop) the cyclomatic complexity was decreased with 50%, from 10 to 5.

- **edmonds_karp@43-80@./algorithms/graph/maximum_flow.py**

    The cyclomatic complexity of the function is 12. The complexity is required to calculate the flow since we need to search through the graph and we have no option but to have a few loops to do this. We can however reduce the cyclomatic complexity splitting the function into smaller units. It exists a while loop that contains a for loop that finds the new flow using BFS, these could be moved to two separate functions. There also exists a while loop that updates the flow array that could also be moved to a third function. This halves the cyclomatic complexity from 12 to 6.

- **intersection@21-64@./algorithms/linkedlist/intersection.py**

    The cyclomatic complexity of the function is 14 and is more or less necessary to be that high. The function is very long since it first has to iterate the linked lists to find which of the two lists are longer. Thereafter, it tries to find a common node where they merge. Since these are two different distinct functionalities, they can be separated into two different functions and subsequently reduce the cyclomatic complexity of the original function. This should lower the complexity since the more complex part of finding information about the lists is moved into another function. 

- **bracket@69-95@./algorithms/strings/breaking_bad.py**

    The cyclomatic complexity of the function is 13. The complexity is necessary because the functionality of the function requires the program to iterate word lists and characters inside those words. It is possible to reduce the complexity by dividing the function into three smaller units: one that creates a symbol dictionary, one that finds matches and lastly the original function which combines the results and returns them.  This will reduce the complexity considerably since the major for loops will be moved into its own function instead of being nested.

- **fix_insert@88-141@./algorithms/tree/red_black_tree/red_black_tree.py**

    The cyclomatic complexity of fix_insert is 11. The high complexity of fix insert is required. In fix insert we need to recolor and or rebalance the tree to follow the red black tree standards after an insert. The red black trees rules about how the tree should be colored and balanced therefore require us to have many different cases to consider. It is however possible to split the function up in multiple smaller units to reduce the complexity. Specifically we could move the code where parent is left of grandparent, and parent is right of grandparent to other functions. This should reduce the complexity with 4 and result in a cyclomatic complexity of 7 which is a decrease of approximately 36 %.

- **delete_fixup@209-269@./algorithms/tree/red_black_tree/red_black_tree.py**

    TODO!!!!!

- **strip_url_params1@14-68@./algorithms/strings/strip_url_params.py**

    The cyclomatic complexity of this function is 20. The complexity is more or less necessary. The function is very long since it checks each parameters length, if it has been added to the resulting url, if it must be removed, etc. It’s possible to reduce this complexity by dividing the code into smaller units. The part of the code that is responsible for checking whether a parameter should be added to the final url (to be returned by the function) can have its own function. Doing this reduces the complexity from 20 to 7 (65% reduction).

- **maximum_flow_bfs@28-84@./algorithms/graph/maximum_flow_dfs.py**

    The cyclomatic complexity of this function is 10. The complexity is necessary because the functionality of the function requires the program to use the dfs algorithms to find a path, get the minimum flow and reduce the capacity. It’s possible to reduce this complexity by dividing the function inte smaller units. The bfs algorithm now has its own function, and so does the part of the code that reduces the capacity. These changes reduces the complexity from 10 to 3 (70% reduction)

## The purpose of each of the high-complexity methods is documented in detail w.r.t. the different out- comes resulting in branches in the code

- **intersection@21-64@./algorithms/linkedlist/intersection.py**

    There is only one test for this function which results in a branch coverage of 66%. The test calls the function with two linked lists of the same length who merge together into a single linked list.

    The test does not try to call the method with two linked lists who do not merge, i.e. two separate linked lists. Additionally, a crucial while loop used when one of the lists is longer than the other is never tested. 

- **bracket@69-95@./algorithms/strings/breaking_bad.py

    There is only one test for the breaking_bad bracket function. It tests an arbitrary input  with three words and three input symbols where a match is found in each word. The tests do not cover cases where, for example, there is no match or where a symbol is mentioned twice in the input (e.g. `[i,i]` could result in a double encapsulation `[[i]]` which is not desired).

- **strip_url_params1@14-68@./algorithms/strings/strip_url_params.py**

    The test suite contains 2 tests, which results in a branch coverage of 85%. Test 1 calls the function with a URL containing 3 parameters (a=1, b=2, a=2), where 2 of them have the same key. The test checks that the same parameter is not used more than one time. Test 2 calls the function with a URL containing 2 parameters (a=1 & b=2) and the parameter to be removed (b). This function checks that the assigned parameter is removed from the url.

    In order to separate the parameters from the rest of the url the character “?” is used. No test covers the case where the function is called with a url not containing this character.

    No test covers the case where the function is called with a url without parameters.

    There is no test that handles the case where the function is called with a parameter (to be removed from the url) and a url with parameters, where the parameter to be removed appears first.

    There is no test that handles the case where the function is called with a url containing a parameter without a key, ex: kth.se?=3. In this case the function should still return a valid url, ex: kth.se  

- **maximum_flow_bfs@28-84@./algorithms/graph/maximum_flow_dfs.py**

    The test suite contains 1 test, which results in 100% branch coverage. The test calls the function with a 6x6 matrix and checks that the correct maximum flow is returned.

- **is_palindrome_dict@52-89@./algorithms/linkedlist/is_palindrome.py**

    For this function there are two assertion tests, consisting of one valid test case and one invalid test case. The branch coverage was 75%. 

- **fix_insert@88-141@./algorithms/tree/red_black_tree/red_black_tree.py**

    No tests exist for any of the red black tree functions and therefore we get a branch coverage of 0%.

- **edmonds_karp@43-80@./algorithms/graph/maximum_flow.py**

    One test exists for edmond karp and has a branch coverage of 100%. The test checks that the flow is correct between two nodes.

- **maximum_flow_bfs@28-84@./algorithms/graph/maximum_flow_bfs.py** 

    There is one corresponding test case for this function and the branch coverage is 100%. The test checks that an expected correct result is returned.


## You create a working ad-hoc coverage tool that at least measures coverage of normal branches (if, while) for ten functions.

Branch coverage was measured by creating a list of integers at the beginning of the function. Afterwards, when a branch was accessed a `1` was placed in the list at the corresponding index of that specific branch. At the end of the function, the list was printed, subsequently showing the branch coverage. If there are multiple tests for a single function you would have to “OR” the list of booleans together and calculate the coverage from the resulting list, see below.

```
[1, 0] OR [0, 1] -> [1, 1] which means 100% coverage
```

1. `What is the quality of your own coverage measurement? Does it take into account ternary operators (condition ? yes : no) and exceptions, if available in your language?`

None of the methods used any ternary operators or exceptions. These operations are available in Python and can be handled by the branch coverage measurement technique if they would have been present. For example, the ternary can be replaced by a normal if statement. Exceptions could be measured like an `if` statement where branch coverage would mean reaching the branch with and without an exception.

2. `What are the limitations of your tool? How would the instrumentation change if you modify the program?`

The limitations of the tool are obvious. Firstly, the tool alters the source code since the list of visited branches has to be updated. Secondly, this also means that if the source code has to change, the branch coverage code would have to be rewritten. Furthermore, the results presented by the tool are basic, it just prints out the list. This means that the programmer has to calculate the branch coverage percentage manually which can be tedious if there are many branches. 

 3. `If you have an automated tool, are your results consistent with the ones produced by existing tool(s)?`

The tool is not automated. However, the results were not always consistent with `coverage.py`. The reason for this is that `coverage.py` measures the branch coverage for the whole file, not singular functions. Files where there was only one function also differed sometimes. This could potentially be because of partial branches which are impossible for `coverage.py` to discover (a partial branch is, for example, a while loop with a return statement inside it or an if statement containing a logical or).
