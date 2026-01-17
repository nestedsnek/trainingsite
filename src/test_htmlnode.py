import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag="div", props={"class": "container", "id": "main"})
        props_html = ''.join(node.props_to_html())
        self.assertEqual(props_html, ' class="container" id="main"')

    def test_repr(self):
        node = HTMLNode(tag="p", value="Hello", children=[], props={"style": "color:red;"})
        expected_repr = "HTMLNode(tag=p, value=Hello, children=[], props={'style': 'color:red;'})"
        self.assertEqual(repr(node), expected_repr)

    def test_to_html_not_implemented(self):
        node = HTMLNode(tag="span")
        with self.assertRaises(NotImplementedError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()
