import pytest

# Needed here because the pages have fucntionality that check in the DB if a user is logged in
from django.core.urlresolvers import reverse
from django.utils.encoding import smart_str

pytestmark = pytest.mark.django_db


def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert "We Help Developers" in smart_str(response.content)
    assert "<title>Recruit Me Now - Home</title>" in smart_str(response.content)


def test_about(client):
    response = client.get('/page/about/')
    assert response.status_code == 200
    assert "About" in smart_str(response.content)
    assert "<title>Recruit Me Now - About</title>" in smart_str(response.content)


def test_info_for_developers(client):
    response = client.get('/page/info-for-developers/')
    assert "About" in smart_str(response.content)
    # probably nicer to change it in the page module: Recruit Me Now - Info For Developers
    assert "<title>Recruit Me Now - Info - For - Developers</title>" in smart_str(response.content)


def test_sitemap(client):
    response = client.get('/page/sitemap/')
    assert response.status_code == 200
    assert "Sitemap" in smart_str(response.content)
    assert "<title>Recruit Me Now - Sitemap</title>" in smart_str(response.content)
