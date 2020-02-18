"""
Given two strings text and pattern,
return the list of  start indexes in text that matches with the pattern
using knuth_morris_pratt algorithm.
If idx is in the list, text[idx : idx + M] matches with pattern.
Time complexity : O(N+M)
N and M is the length of text and pattern, respectively.
"""

def knuth_morris_pratt(text, pattern):
    checked = 0
    visited_Branches = [0] * 10
    print("\n")

    n = len(text)
    m = len(pattern)
    pi = [0 for i in range(m)]
    i = 0
    j = 0
    # making pi table
    for i in range(1, m):
        visited_Branches[0] = 1
        while j and pattern[i] != pattern[j]:
            visited_Branches[1] = 1
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            visited_Branches[2] = 1
            j += 1
            pi[i] = j
        else:
            visited_Branches[3] = 1
    # finding pattern
    j = 0
    ret = []
    for i in range(n):
        visited_Branches[4] = 1
        while j and text[i] != pattern[j]:
            visited_Branches[5] = 1
            j = pi[j - 1]
        if text[i] == pattern[j]:
            visited_Branches[6] = 1
            j += 1
            if j == m:
                visited_Branches[7] = 1
                ret.append(i - m + 1)
                j = pi[j - 1]
            else:
                visited_Branches[8] = 1
        else:
            visited_Branches[9] = 1
    
    for i in range(len(visited_Branches)):
        checked += (1 if visited_Branches[i] == 1 else 0)
    
    print(visited_Branches)
    print(str(checked/len(visited_Branches))+"%")

    return ret
