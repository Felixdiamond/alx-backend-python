#!/usr/bin/env python3
"""This module contains the TestGithubOrgClient class for testing the
GithubOrgClient.org method.
"""

from typing import Any, Dict
import unittest
from unittest.mock import Mock, patch, PropertyMock
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

    def test_public_repos_url(self):
        """Tests that GithubOrgClient._public_repos_url returns the correct
        value"""
        expected_result = "https://api.github.com/orgs/google/repos"
        payload = {"repos_url": expected_result}
        with patch('client.GithubOrgClient.org', PropertyMock(
            return_value=payload
        )):
            github_client = GithubOrgClient("google")
            self.assertEqual(github_client._public_repos_url,
                             expected_result)

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """Tests that GithubOrgClient.public_repos returns the
        correct value"""
        json_payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_json.return_value = json_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public:

            mock_public.return_value = "hello/world"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            check = [i["name"] for i in json_payload]
            self.assertEqual(result, check)

            mock_public.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self,
                         repo: Dict[str,
                                    Any],
                         license_key: str,
                         expected_result: bool):
        """Tests that GithubOrgClient.has_license returns the correct value"""
        self.assertEqual(
            GithubOrgClient.has_license(
                repo,
                license_key),
            expected_result)
