import pytest
import requests_mock
import json

from tests.unit_tests.helpers import read_file

pytestmark = pytest.mark.django_db
TRAVIS_FAIL_REASON = "Will fail on Travis (no external connection)"


@pytest.mark.xfail(reason=TRAVIS_FAIL_REASON)
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


@pytest.mark.xfail(reason=TRAVIS_FAIL_REASON)
def test_update_bitbucket_repo_info(developer):
    # Not needed check: but let's make sure for the demo:
    assert not developer.bitbucket_repo_info

    # BAD BAD BAD Practice -> always avoid real calls in your testing setup!
    # Will fail without internet!
    developer.update_bitbucket_repo_info()

    # Check if content arrived in model:
    assert "acidjunk" in str(developer.bitbucket_repo_info)
    assert "acidjunk_mocked" not in str(developer.bitbucket_repo_info)

    # Will break when I add/remove a public repo
    assert len(developer.bitbucket_repo_info) == 2


def test_update_bitbucket_repo_info_mocked(developer):
    # Not needed check: but let's make sure for the demo:
    assert not developer.bitbucket_repo_info

    bitbucket_repo_info_str = read_file("bitbucket_repo_info.json")

    with requests_mock.mock() as m:
        m.get("https://bitbucket.org/api/2.0/repositories/acidjunk", text=bitbucket_repo_info_str)
        developer.update_bitbucket_repo_info()

    assert "acidjunk" in str(developer.bitbucket_repo_info)
    assert len(developer.bitbucket_repo_info) == 2


def test_update_bitbucket_repo_info_mocked_check_for_next(developer):
    # Not needed check: but let's make sure for the demo:
    assert not developer.bitbucket_repo_info

    bitbucket_repo_info_str = read_file("bitbucket_repo_info.json")
    bitbucket_repo_info = json.loads(bitbucket_repo_info_str)
    bitbucket_repo_info["next"] = "this_triggers_a_not_implemented_error"

    with requests_mock.mock() as m2, pytest.raises(NotImplementedError):
        m2.get("https://bitbucket.org/api/2.0/repositories/acidjunk", text=json.dumps(bitbucket_repo_info))
        developer.update_bitbucket_repo_info()