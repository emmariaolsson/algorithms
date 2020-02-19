# Complexity measurement

1.  `What are your results? Did everyone get the same result? Is there something that is unclear? If you have a tool, is its result the same as yours?`

### Lizard CC

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


### Manually counted cyclomatic complexity

- *is_palindrome_dict@52-89@./algorithms/linkedlist/is_palindrome.py*

    The cyclomatic complexity of the function is 10, according to Mccabe’s formula M = pi - s + 2, where π = 12 and s = 4. It coincides with the results from lizard.

- *edmonds_karp@43-80@./algorithms/graph/maximum_flow.py*
    
    The cyclomatic complexity of the function is 12. The same value was calculated using Mccabe’s formula with π = 11 and s = 1.

- *intersection@21-64@./algorithms/linkedlist/intersection.py*
    
    The cyclomatic complexity of the function is 14 according to lizard. By using McCabe’s formula we count a cyclomatic complexity of 13, where π = 13, s = 2. 

- *fix_insert@88-141@./algorithms/tree/red_black_tree/red_black_tree.py*
    
    The cyclomatic complexity according to lizard is 11. Using McCabe’s formula we get with π = 10, s = 1: M = 10-1+2= 11

- *delete_fixup@209-269@./algorithms/tree/red_black_tree/red_black_tree.py*
    
    The cyclomatic complexity of the function is 18. Using McCabe’s formula with π = 16 and s = 0 we also get 18.

2.  `Are the functions/methods with high CC also very long in terms of LOC?`

    In general, yes but there are exceptions where short functions have high CC.

3.  `What is the purpose of these functions? Is it related to the high CC?`

- *is_palindrome_dict@52-89@./algorithms/linkedlist/is_palindrome.py*
    
    The function determines if a linked list is a palindrome. It does this by constructing a dictionary where the keys are the values of the list, and the values are the positions at which these values occur in the list. It determines if the linked list is a palindrome by iterating the dictionary and making sure certain criteria are met. 

- *edmonds_karp@43-80@./algorithms/graph/maximum_flow.py*

    In a graph it computes the maximum flow between source and sink using BFS. This requires a high CC since it needs to search through the graph and many branches are possible.

- *intersection@21-64@./algorithms/linkedlist/intersection.py*

    The purpose of the intersection method is to find the common node from two linked lists, i.e. the intersecting node. 

- *fix_insert@88-141@./algorithms/tree/red_black_tree/red_black_tree.py*

    When inserting a node into a red-black tree the color of the tree needs to be updated to work with the new node according to the rules of coloring a red-black tree. This means that we need to look at the color of the relatives of the inserted node to figure out how we should recolor the graph. Depending on the current colors of the relatives we therefore take different paths and a high CC is required.

- *delete_fixup@209-269@./algorithms/tree/red_black_tree/red_black_tree.py*

    When deleting a node the color of the red black tree also needs to be updated. Just like when fixing insert we also need to go over the graph and color the graph differently depending on the color of the removed node and its relatives which gives us by necessity a high CC.


4.  `If your programming language uses exceptions: Are they taken into account by the tool? If you think of an exception as another possible branch (to the catch block or the end of the function), how is the CC affected?`

    Python uses exceptions and they are taken into account by the tool. This was tested by measuring the CC for a method that only had a single return and comparing it with a method that had a `try/catch` and a return. The test showed that the `try/catch` increases the CC by one.

5.  `Is the documentation of the function clear about the different possible outcomes induced by different branches taken?`

    Some of the functions are very well documented. For example, the linked list intersection function clearly describes how it works and when it returns true or false. However, the documentation is not as good for most of the functions. In these cases, the programmer reading the code has to figure out the possible outcomes induced by the branching. 

