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

    def test_public_repos(self, mock_get_json):
        """Tests that GithubOrgClient.public_repos returns the correct
        value"""
        expected_result = ["repo1", "repo2"]
        mock_get_json.return_value = [{"name": "repo1"}, {"name": "repo2"}]
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            url = "https://api.github.com/orgs/google/repos"
            mock_public_repos_url.return_value = url
            github_client = GithubOrgClient("google")
            self.assertEqual(github_client.public_repos, expected_result)
            mock_get_json.assert_called_once()
            mock_public_repos_url.assert_called_once()
