# -*- coding: utf-8 -*-
import simplejson

TYPE = 'oauth2'
NAME = 'registr'
DISPLAY_NAME = u'Registr Svobodných'
TOOLTIP_TEXT = u'Pokud jste člen nebo příznivec Svobodných, přihlaste se pomocí Registru'
ICON_MEDIA_PATH = '/upfiles/registr.png'

OAUTH_ENDPOINT = 'https://registr.svobodni.cz/oauth/authorize'
OAUTH_TOKEN_ENDPOINT = 'https://registr.svobodni.cz/oauth/token'
OAUTH_RESOURCE_ENDPOINT = 'https://registr.svobodni.cz/auth/'


def oauth_get_user_id_function(client):
    return client.request('profile.json')['person']['id']

def response_parser(json):
    return simplejson.loads(json)