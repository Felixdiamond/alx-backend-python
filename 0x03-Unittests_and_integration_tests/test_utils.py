#!/usr/bin/env python3
"""This module contains the TestAccessNestedMap class for testing the
utils.access_nested_map function.
"""

import unittest
from parameterized import parameterized
import utils
from typing import Any, Dict, Tuple


class TestAccessNestedMap(unittest.TestCase):
    """This class contains test cases for the utils.access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: dict, path: tuple,
                               expected_output: any) -> None:
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
    @unittest.mock.patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Tests get_json with different inputs"""
        mock_get.return_value.json.return_value = test_payload
        self.assertEqual(utils.get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)
