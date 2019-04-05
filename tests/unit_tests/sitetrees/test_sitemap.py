import pytest
from django.core.urlresolvers import reverse

pytestmark = pytest.mark.django_db


def test_sitemap(client):
    response = client.get('/page/sitemap/')
    assert response.status_code == 200
