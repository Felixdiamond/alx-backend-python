#!/usr/bin/env python3
"""This module contains the TestAccessNestedMap class for testing the utils.access_nested_map function."""

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
    def test_access_nested_map(self, nested_map: dict, path: tuple, expected_output: any) -> None:
        """Tests that the utils.access_nested_map function returns the expected output for given inputs."""
        self.assertEqual(utils.access_nested_map(nested_map, path), expected_output)

