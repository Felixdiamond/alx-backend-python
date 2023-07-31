#!/usr/bin/env python3
"""This module contains the TestAccessNestedMap class for testing the
utils.access_nested_map function.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
import utils
from utils import get_json
from utils import memoize
from typing import Any, Dict, Tuple


class TestAccessNestedMap(unittest.TestCase):
    """This class contains test cases for the utils.access_nested_map
    function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Dict, path: Tuple,
                               expected_output: Any) -> None:
        """Tests that the utils.access_nested_map function returns the expected
        output for given inputs.
        """
        self.assertEqual(
            utils.access_nested_map(nested_map, path),
            expected_output
        )

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict[str, Any],
            path: Tuple[str, ...]
    ) -> None:
        """Tests that access_nested_map raises a KeyError for invalid inputs
        """
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Tests the get_json function from the utils module"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str,
                      test_payload: Dict[str, Any]) -> None:
        """Tests get_json with different inputs"""
        config = {'return_value.json.return_value': test_payload}
        patcher = patch('requests.get', **config)
        mock = patcher.start()
        self.assertEqual(get_json(test_url), test_payload)
        mock.assert_called_once_with(test_url)
        patcher.stop()


class TestMemoize(unittest.TestCase):
    """Tests the memoize decorator from the utils module"""

    def test_memoize(self):
        """Tests that the memoize decorator correctly caches the result of
        a method"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method',
                          return_value=42) as mock_method:
            test_class = TestClass()
            self.assertEqual(test_class.a_property, 42)
            self.assertEqual(test_class.a_property, 42)
            mock_method.assert_called_once()
