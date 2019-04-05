from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.utils import timezone

import pytest
from rest_framework.test import APIClient
from tests.unit_tests import factories


pytestmark = pytest.mark.django_db

# Some constants
USER_PASS = "Fr3d_1234"
ADMIN_PASS = "@dmin_1234"


# @pytest.fixture
# def sitetree(admin_user):
#     sitetree_fixture = path_join(dirname(dirname(__file__)), 'sitetree.json')
#
#     st = loads(open(sitetree_fixture).read())
#
#     sitetree = factories.SiteTreeFactory.create(**st[0]['fields'])
#     # Items are sorted on primary key to avoid parent references to an item that is not yet present.
#     for item in sorted(st[1:], key=lambda i: int(i['pk'])):
#         item['fields']['id'] = item['pk']
#         item['fields']['tree'] = sitetree
#         parent = item['fields']['parent']
#         item['fields']['parent_id'] = parent
#         del item['fields']['parent']
#         del item['fields']['access_permissions']
#         factories.SiteTreeItemFactory.create(**item['fields'])
#
#     return sitetree

@pytest.fixture
def admin_user():
    return get_user_model().objects.create_superuser(
        username="admin",
        email="admin@example.com",
        password=ADMIN_PASS)

@pytest.fixture
def user():
    # TODO: maybe a normal user is better?
    return get_user_model().objects.create_user(
        username="fred",
        email="fred@formatics.nl",
        password=USER_PASS)


@pytest.fixture
def user_client(user, client):
    response = client.post(reverse('login'), data={'username': 'fred', 'password': USER_PASS})
    assert response.status_code == 302
    return client


@pytest.fixture
def admin_rest_client(admin_user):
    """
    Fixture to test REST API Calls used for tests with admin user
    """
    client = APIClient()
    assert client.login(username='admin', password=ADMIN_PASS)
    return client


@pytest.fixture
def user_rest_client(user):
    """
    Fixture to test REST API Calls used for tests with user: fred (without development reference)
    """
    client = APIClient()
    assert client.login(username="fred", password=USER_PASS)
    return client


@pytest.fixture
def developer_rest_client(developer):
    """
    Fixture to test REST API Calls used for tests with user/developer: fred
    """

    client = APIClient()
    assert client.login(username="fred", password=USER_PASS)
    return client


@pytest.fixture
def developer(user):
    """One Developer object with a reference to the Django user."""
    return factories.DeveloperFactory.create(
        user=user,
        slug="developer-slug",
        birth_date=timezone.now(),
        bio="One of the fastest single thread developers known to exists. His single "
            "core, single thread, strategy lets him focus on just what it's in front of him.",
        profile_title="Developer",
        linkedin_profile="https://linkedin.com/profiles/fred",
        github_profile="https://github.com/acidjunk",
        created_by=user,
        created_on=timezone.now(),
        modified_by=user,
        modified_on=timezone.now())
