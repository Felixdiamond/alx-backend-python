#!/usr/bin/env python3
"""This module contains the TestGithubOrgClient class for testing the
GithubOrgClient.org method.
"""

from typing import Any, Dict, List
import unittest
from unittest.mock import Mock, patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Class for Integration test of fixtures """

    @classmethod
    def setUpClass(cls):
        """A class method called before tests in an individual class are run"""

        config = {'return_value.json.side_effect':
                  [
                      cls.org_payload, cls.repos_payload,
                      cls.org_payload, cls.repos_payload
                  ]
                  }
        cls.get_patcher = patch('requests.get', **config)

        cls.mock = cls.get_patcher.start()

    def test_public_repos(self):
        """ Integration test: public repos"""
        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.org, self.org_payload)
        self.assertEqual(test_class.repos_payload, self.repos_payload)
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """ Integration test for public repos with License """
        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.assertEqual(test_class.public_repos(
            "apache-2.0"), self.apache2_repos)
        self.mock.assert_called()

    @classmethod
    def tearDownClass(cls):
        """A class method called after tests in an individual class have run"""
        cls.get_patcher.stop()
