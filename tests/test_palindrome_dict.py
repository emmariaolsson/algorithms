import unittest

from algorithms.linkedlist import is_palindrome_dict

class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Convert from linked list Node to list for testing
def convert(head):
    ret = []
    if head:
        current = head
        while current:
            ret.append(current.val)
            current = current.next
    return ret

class TestSuite(unittest.TestCase):

    def test_if_palindrome_dict_positive(self):
        self.l = Node('A')
        self.l.next = Node('B')
        self.l.next.next = Node('C')
        self.l.next.next.next = Node('B')
        self.l.next.next.next.next = Node('A')
        self.assertTrue(is_palindrome_dict(self.l))

    def test_if_palindrome_dict_negative(self):
        self.l1 = Node('A')
        self.l1.next = Node(1)
        self.l1.next.next = Node('C')
        self.l1.next.next.next = Node('B')
        self.l1.next.next.next.next = Node('A')
        self.assertFalse(is_palindrome_dict(self.l1))
    """
    def test_if_palindrome_dict_empty(self):
        self.l2 = Node("") #This case needs to be scrutinized. Node() returns error.
        run = is_palindrome_dict(self.l2)
        self.assertTrue(run)

        
    def test_if_palindrome_dict_single(self):
        self.l3 = Node('A')            
        self.assertTrue(is_palindrome_dict(self.l3))
    """
        

if __name__ == "__main__":
    unittest.main()
    
