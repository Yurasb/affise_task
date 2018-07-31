from tests.helpers import HEADERS, call_pixel


def test_pixel_positive():
    response = call_pixel(headers=HEADERS)
    assert response.status_code == 200


def test_pixel_wrong_key():
    header = {'api-key': 'th1s1sth3wr0ngk3y'}
    response = call_pixel(headers=header)
    assert response.status_code == 403


def test_pixel_get():
    response = call_pixel(method='GET', headers=HEADERS)
    assert response.status_code == 405
