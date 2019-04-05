import pytest
from django.core.urlresolvers import reverse
from tests.unit_tests.helpers import assert_rest_detail

pytestmark = pytest.mark.django_db()


class TestRestApi(object):
    def test_list_api_admin(self, admin_rest_client, developer):
        response = admin_rest_client.get("/api/users/", format="json")
        assert response.status_code == 200

        # 2 users: `admin` and `fred`
        assert len(response.data["results"]) == 2
        assert response.data["count"] == 2


    def test_detail_api_admin(self, admin_rest_client, admin_user):
        expected_result = {"url": "http://testserver/api/users/{}/".format(admin_user.pk),
                           "username": "admin", 
                           "email": "admin@example.com",
                           "groups": []}
        url = reverse('user-detail', kwargs={'pk': admin_user.pk})
        assert_rest_detail(admin_rest_client, url, expected_result)
