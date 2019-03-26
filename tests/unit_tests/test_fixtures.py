# Just some general asserts to test the integrity of the fixtures
import pytest

pytestmark = pytest.mark.django_db


def test_developer(developer):
    assert developer.profile_title == "Developer"
