from tests.helpers import HEADERS, call_offers


def test_offers_positive():
    response = call_offers(headers=HEADERS)
    assert response.status_code == 200


def test_offers_wrong_key():
    header = {'api-key': 'th1s1sth3wr0ngk3y'}
    response = call_offers(headers=header)
    assert response.status_code == 403


def test_offers_post():
    response = call_offers(method='POST', headers=HEADERS)
    assert response.status_code == 405
