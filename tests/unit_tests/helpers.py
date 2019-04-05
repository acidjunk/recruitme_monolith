from os.path import dirname, join, realpath
import pytest

from django.core.urlresolvers import reverse


def read_file(file_name, folder="mocks"):
    file = join(dirname(realpath(__file__)), folder, file_name)
    with open(file) as f:
        return f.read()


def assert_responses(client, expected_code, url_names, kwargs={}, prefix_urls='', suffix_urls=''):
    """
    Helper function to test a bunch of pages with specific kwargs

    :param expected_code: expected http response code (e.g. 200 or 302 or a tuple of codes)
    :param url_names: List of url names (e.g. ['about', 'info'])
    :param kwargs: dict e.g. {'pk': 1}
    :param prefix_urls: 'appname:'
    :param suffix_urls: query string, does not get evaluated '?change=asdf'
    :return:
    """
    for page in url_names:
        url = '{}{}'.format(reverse('{}{}'.format(prefix_urls, page), kwargs=kwargs), suffix_urls)
        response = client.get(url)

        if isinstance(expected_code, int):
            # expected_code can either be a tuple or a single integer.
            expected_code = (expected_code,)

        print(prefix_urls, page, expected_code, response.status_code)
        assert response.status_code in expected_code, \
            '{} failed. expected {}, got {} for page {} with reason {}'\
            .format(url, expected_code, response.status_code, page, response.__dict__)


def assert_rest_detail(rest_client, url, expected_data):
    response = rest_client.get(url)
    # make sure that in case of an error you can see the json response if any
    assert response.content
    assert response.status_code == 200, response.content

    for key, expected_result in expected_data.items():
        assert response.data.get(key) == expected_result, response.data
