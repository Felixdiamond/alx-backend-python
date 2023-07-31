#!/usr/bin/env python3
"""This module contains the TestGithubOrgClient class for testing the
GithubOrgClient.org method.
"""

from typing import Any, Dict
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """Tests the GithubOrgClient class"""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"})
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, expected_result: Dict[str, Any],
                 mock_get_json: Mock) -> None:
        """Tests that GithubOrgClient.org returns the correct value"""
        mock_get_json.return_value = expected_result
        github_client = GithubOrgClient(org_name)
        self.assertEqual(github_client.org, expected_result)
        url = f'https://api.github.com/orgs/{org_name}'
        mock_get_json.assert_called_once_with(url)

