
def is_palindrome_dict(head):
    """
    This function builds up a dictionary where the keys are the values of the list,
    and the values are the positions at which these values occur in the list.
    We then iterate over the dict and if there is more than one key with an odd
    number of occurrences, bail out and return False.
    Otherwise, we want to ensure that the positions of occurrence sum to the
    value of the length of the list - 1, working from the outside of the list inward.
    For example:
    Input: 1 -> 1 -> 2 -> 3 -> 2 -> 1 -> 1
    d = {1: [0,1,5,6], 2: [2,4], 3: [3]}
    '3' is the middle outlier, 2+4=6, 0+6=6 and 5+1=6 so we have a palindrome.
    """
    branches = [0]*12
    if not head: 
        branches[0] = 1
        codeCoverage(branches)
        return True
    elif not head.next:
        branches[1] = 1
        codeCoverage(branches)
        return True
    d = {}
    pos = 0
    while head:
        branches[2] = 1
        if head.val in d.keys():
            branches[3] = 1        
            d[head.val].append(pos)
        else:
            branches[4] = 1    
            d[head.val] = [pos]
        head = head.next
        pos += 1
    checksum = pos - 1
    middle = 0
    for v in d.values():
        branches[5] = 1
        if len(v) % 2 != 0:
            branches[6] = 1    
            middle += 1
        else:
            branches[7] = 1
            step = 0
            for i in range(0, len(v)):
                branches[8] = 1
                if v[i] + v[len(v) - 1 - step] != checksum:
                    branches[9] = 1
                    codeCoverage(branches)
                    return False
                step += 1
        if middle > 1:
            branches[10] = 1
            codeCoverage(branches)
            return False
        else:
            branches[11] = 1
    codeCoverage(branches)
    return True

def codeCoverage(branches):
    print("------ Check out this coverage: ------")
    print(branches)
    