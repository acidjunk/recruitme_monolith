import pytest

from django.core.urlresolvers import reverse
pytestmark = pytest.mark.django_db


def test_developer_list_view(user_client, developer):
    response = user_client.get(reverse('developers:developer-list'))
    assert response.status_code == 200


def test_developer_detail_view_by_slug(user_client, developer):
    response = user_client.get(reverse('developers:developer-detail', args=[developer.slug]))
    assert response.status_code == 200


def test_developer_detail_view_by_slug_404(user_client, developer):
    response = user_client.get(reverse('developers:developer-detail', args=["chuck-norris-ninja-coder"]))
    assert response.status_code == 404


def test_developer_list_view_no_permission(admin_client, developer):
    response = admin_client.get(reverse('developers:developer-list'))
    assert response.status_code == 302


def test_developer_detail_view_by_slug_no_permission(admin_client, developer):
    response = admin_client.get(reverse('developers:developer-detail', args=[developer.slug]))
    assert response.status_code == 302
