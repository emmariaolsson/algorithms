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
    if not head: 
        return True 
    if not head.next:
        return True
    d = {}
    pos = 0
    while head:
        fill_dict(head, d, pos)
        head = head.next
        pos += 1
    checksum = pos - 1
    middle = 0
    for v in d.values():
        if len(v) % 2 != 0:
            middle += 1
        else:
            step = 0
            for i in range(0, len(v)):
                if v[i] + v[len(v) - 1 - step] != checksum:
                    return False
                step += 1
        if middle > 1:
            return False
    return True

def fill_dict(head, d, pos):
    if head.val in d.keys():
        d[head.val].append(pos)
    else:
        d[head.val] = [pos]
