from algorithms.tree.traversal import (
    preorder,
    preorder_rec,
    postorder,
    postorder_rec,
    inorder,
    inorder_rec
)
from algorithms.tree.b_tree import BTree
from algorithms.tree.red_black_tree.red_black_tree import RBTree, RBNode

import unittest


class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TestTraversal(unittest.TestCase):

    def test_preorder(self):
        tree = create_tree()
        self.assertEqual([100, 50, 25, 75, 150, 125, 175], preorder(tree))
        self.assertEqual([100, 50, 25, 75, 150, 125, 175], preorder_rec(tree))

    def test_postorder(self):
        tree = create_tree()
        self.assertEqual([25, 75, 50, 125, 175, 150, 100], postorder(tree))
        self.assertEqual([25, 75, 50, 125, 175, 150, 100], postorder_rec(tree))

    def test_inorder(self):
        tree = create_tree()
        self.assertEqual([25, 50, 75, 100, 125, 150, 175], inorder(tree))
        self.assertEqual([25, 50, 75, 100, 125, 150, 175], inorder_rec(tree))


def create_tree():
    n1 = Node(100)
    n2 = Node(50)
    n3 = Node(150)
    n4 = Node(25)
    n5 = Node(75)
    n6 = Node(125)
    n7 = Node(175)
    n1.left, n1.right = n2, n3
    n2.left, n2.right = n4, n5
    n3.left, n3.right = n6, n7
    return n1


class TestBTree(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        import random
        random.seed(18719)
        cls.random = random
        cls.range = 10000

    def setUp(self):
        self.keys_to_insert = [self.random.randrange(-self.range, self.range) for i in range(self.range)]

    def test_insertion_and_find_even_degree(self):
        btree = BTree(4)
        for i in self.keys_to_insert:
            btree.insert_key(i)

        for i in range(100):
            key = self.random.choice(self.keys_to_insert)
            self.assertTrue(btree.find(key))

    def test_insertion_and_find_odd_degree(self):
        btree = BTree(3)
        for i in self.keys_to_insert:
            btree.insert_key(i)

        for i in range(100):
            key = self.random.choice(self.keys_to_insert)
            self.assertTrue(btree.find(key))

    def test_deletion_even_degree(self):
        btree = BTree(4)
        key_list = set(self.keys_to_insert)
        for i in key_list:
            btree.insert_key(i)

        for key in key_list:
            btree.remove_key(key)
            self.assertFalse(btree.find(key))

        self.assertEqual(btree.root.keys, [])
        self.assertEqual(btree.root.children, [])

    def test_deletion_odd_degree(self):
        btree = BTree(3)
        key_list = set(self.keys_to_insert)
        for i in key_list:
            btree.insert_key(i)

        for key in key_list:
            btree.remove_key(key)
            self.assertFalse(btree.find(key))

        self.assertEqual(btree.root.keys, [])
        self.assertEqual(btree.root.children, [])

class TestRedBlackTree(unittest.TestCase):
    #Check that with a null parent node color is 0 and node is root
    def test_parent_null(self):
        node = RBNode(5,0)
        node.parent = None
        rb = RBTree()
        rb.fix_insert(node)
        self.assertTrue(node.color == 0)
        self.assertTrue(rb.root == node)
        
     #Check that with a black parent do nothing
    def test_parent_black(self):
        rb = RBTree()
        node = RBNode(5,0)
        node.parent = RBNode(2, 0)
        rb.root = node.parent
        rb.fix_insert(node)
        self.assertTrue(node.color == 0)
        self.assertTrue(node.val == 5)
 
    #Check that with a red parent, red uncle, whole tree should be black
    def test_parent_red_uncle_red(self):
        rb = RBTree()
        node = RBNode(5,0)
        node.parent = RBNode(2, 1)
        node.parent.left = node
        node.parent.parent = RBNode(2, 0)
        node.parent.parent.left = node.parent
        node.parent.parent.right = RBNode(1, 1)
        rb.root = node.parent.parent
        rb.fix_insert(node)
        self.assertTrue(rb.root.color == 0)
        self.assertTrue(rb.root.left.color == 0)
        self.assertTrue(rb.root.right.color == 0)
        self.assertTrue(rb.root.left.left.color == 0)

        
    #Check that with a red parent thats right of grandparent, 
    # and black uncle left of grandparent, 
    # Parent and node should be left instead of right
    # and color of parent should be red
    def test_parent_red_uncle_black(self):
        rb = RBTree()
        node = RBNode(5,0)
        node.parent = RBNode(2, 1)
        node.parent.parent = RBNode(2, 0)
        node.parent.parent.left = RBNode(1, 0)
        node.parent.parent.right = node.parent
        rb.root = node.parent.parent
        rb.fix_insert(node)
        self.assertTrue(rb.root.color == 0)
        self.assertTrue(rb.root.left.color == 1)
        self.assertTrue(rb.root.left.left.color == 0)
     
if __name__ == '__main__':
    unittest.main()
