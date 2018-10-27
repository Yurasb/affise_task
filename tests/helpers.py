from requests import request


BASE_URL = 'http://api.staging.affise.com/3.0/partner'
HEADERS = {'api-key': 'caf1d63d471929d1f3dd8ac17578e9fe0458f4a3'}
DATA = ('pid=610&offer_id=906&name=test&code=<script>test</script>&'
        'code_type=javascript')


def call_offers(**kwargs):
    if 'method' not in kwargs:
        resp = request(
            url='{}/offers'.format(BASE_URL),
            method='GET',
            headers=kwargs['headers']
        )
    else:
        resp = request(
            url='{}/offers'.format(BASE_URL),
            method=kwargs['method'],
            headers=kwargs['headers']
        )
    return resp


def call_pixel(**kwargs):
    if 'method' not in kwargs:
        resp = request(
            url='{}/pixel'.format(BASE_URL),
            method='POST',
            headers=kwargs['headers'],
            data=DATA
        )
    else:
        resp = request(
            url='{}/pixel'.format(BASE_URL),
            method=kwargs['method'],
            headers=kwargs['headers']
        )
    return resp
