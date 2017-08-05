import secret


def get_api_key():
    return secret.get_key('google_search_api_key')


def get_cx():
    return secret.get_key('google_cx')
