import json

import pytest
import requests_mock

from recruitme.apps.developers.models import Developer
from tests.unit_tests.helpers import read_file

pytestmark = pytest.mark.django_db


def test_update_github_repo_info(developer):
    # Not needed check: but let's make sure for the demo:
    assert not developer.github_repo_info

    # BAD BAD BAD Practice -> always avoid real calls in your testing setup!
    # Will fail without internet!
    developer.update_github_repo_info()

    # Check if content arrived in model:
    assert "acidjunk" in str(developer.github_repo_info)
    assert "acidjunk_mocked" not in str(developer.github_repo_info)

    # Will break when I add/remove a public repo
    assert len(developer.github_repo_info) == 30


def test_update_github_repo_info_mocked(developer):
    # Not needed check: but let's make sure for the demo:
    assert not developer.github_repo_info

    with requests_mock.mock() as m:
        m.get("https://api.github.com/users/acidjunk/repos", text=read_file("github_repo_info.json"))
        developer.update_github_repo_info()

    # Check if content arrived in model:
    assert "acidjunk" in str(developer.github_repo_info)
    assert "acidjunk_mocked" in str(developer.github_repo_info)
    assert len(developer.github_repo_info) == 2
