import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("h1", "Hello World", None, {'href': 'http://www.mytesturl.com'})
        self.assertEqual(repr(node), "HTMLNode(h1, Hello World, None, {'href': 'http://www.mytesturl.com'})")

    def test_to_html(self):
        html_node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            html_node.to_html()

    def test_props_to_html(self):
        html_node = HTMLNode(None, None, None, {'href': 'https://www.google.com', 'target': '_blank'})
        self.assertEqual(html_node.props_to_html(),  "href=\"https://www.google.com\" target=\"_blank\"")

if __name__ == "__main__":
    unittest.main()
