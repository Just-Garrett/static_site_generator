import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        # Should be True
        self.assertEqual(node, node2)
        node3 = TextNode("This is a text node", "bold", None)
        # Should be True. None url property should match empty argument
        self.assertEqual(node, node3)
        node4 = TextNode("This is a text node", "bold", "http://boot.dev")
        # Should be True. Empty url argument should not match given url argument 
        self.assertNotEqual(node, node4)
        # Should be True. None url argument should not match given url argument
        self.assertNotEqual(node3, node4)
        node5 = TextNode("This is a different text node", "bold")
        node6 = TextNode("This is a text node", "italic")
        # Should be True. Different text argument.
        self.assertNotEqual(node, node5)
        # Should be True. Different text_type argument
        self.assertNotEqual(node, node6)

if __name__ == "__main__":
    unittest.main()
