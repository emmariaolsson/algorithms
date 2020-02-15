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
    #Original testcase
    def test_if_palindrome_dict_positive(self):
        self.l = Node('A')
        self.l.next = Node('B')
        self.l.next.next = Node('C')
        self.l.next.next.next = Node('B')
        self.l.next.next.next.next = Node('A')
        self.assertTrue(is_palindrome_dict(self.l))
    #Original testcase
    def test_if_palindrome_dict_negative(self):
        self.l1 = Node('A')
        self.l1.next = Node('B')
        self.l1.next.next = Node('C')
        self.l1.next.next.next = Node('B')
        self.assertFalse(is_palindrome_dict(self.l1))
        
    #Suppose to cover branch 10 (if middle > 1)
    def test_if_palindrome_dict_middle(self):
        self.l2 = Node('A')
        self.l2.next = Node('B')
        self.l2.next.next = Node('C')
        self.l2.next.next.next = Node('D')
        self.l2.next.next.next.next = Node('A')
        self.assertFalse(is_palindrome_dict(self.l2))

    #Suppose to cover branch 0 (if not head)
    def test_if_palindrome_dict_None(self):
        self.assertTrue(is_palindrome_dict(None))

    #Suppose to cover branch 1 (if not head.next)    
    def test_if_palindrome_dict_single(self):
        self.l3 = Node('A')            
        self.assertTrue(is_palindrome_dict(self.l3))
    
        

if __name__ == "__main__":
    unittest.main()

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
    #Original testcase
    def test_if_palindrome_dict_positive(self):
        self.l = Node('A')
        self.l.next = Node('B')
        self.l.next.next = Node('C')
        self.l.next.next.next = Node('B')
        self.l.next.next.next.next = Node('A')
        self.assertTrue(is_palindrome_dict(self.l))
    #Original testcase
    def test_if_palindrome_dict_negative(self):
        self.l1 = Node('A')
        self.l1.next = Node('B')
        self.l1.next.next = Node('C')
        self.l1.next.next.next = Node('B')
        self.assertFalse(is_palindrome_dict(self.l1))

    def test_if_palindrome_dict_middle(self):
        self.l2 = Node('A')
        self.l2.next = Node('B')
        self.l2.next.next = Node('C')
        self.l2.next.next.next = Node('D')
        self.l2.next.next.next.next = Node('A')
        self.assertFalse(is_palindrome_dict(self.l2))

    #Suppose to cover branch 0 (if not head)
    def test_if_palindrome_dict_None(self):
        self.assertTrue(is_palindrome_dict(None))

    #Suppose to cover branch 1 (if not head.next)    
    def test_if_palindrome_dict_single(self):
        self.l3 = Node('A')            
        self.assertTrue(is_palindrome_dict(self.l3))
    
        

if __name__ == "__main__":
    unittest.main()
    

    
