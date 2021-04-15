import unittest
import json_flatten

# Account for difference in boolean capitalisation between Python and JSONs
true = True
false = False


class TestFlatten(unittest.TestCase):

    def test_flat_json(self):
        self.assertEqual(json_flatten.flatten({"a": 1, "b": true}), '{"a": 1, "b": true}')

    def test_nested_json(self):
        self.assertEqual(json_flatten.flatten({"a": 1, "b": {"c": "hello", "d":4}, "e": true}), '{"a": 1, "b.c": "hello", "b.d": 4, "e": true}')

    def test_double_layered_nested_json(self):
        self.assertEqual(json_flatten.flatten({"a": 1, "b": {"c": "hello", "d":{"e": true, "f":6}, "g":"seven"}}), '{"a": 1, "b.c": "hello", "b.d.e": true, "b.d.f": 6, "b.g": "seven"}')
 
    def test_2_nested_json(self):
        self.assertEqual(json_flatten.flatten({"a": 1, "b": {"c": "hello", "d":4}, "e": {"f": false, "g":"example"}}), '{"a": 1, "b.c": "hello", "b.d": 4, "e.f": false, "e.g": "example"}')
