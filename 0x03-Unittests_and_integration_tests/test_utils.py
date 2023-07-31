#!/usr/bin/env python3
"""This module contains the TestAccessNestedMap class for testing the
utils.access_nested_map function.
"""

from typing import Any, Dict, Tuple
import unittest
from parameterized import parameterized
import utils


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
            access_nested_map(nested_map, path)
