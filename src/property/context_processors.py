from env.api_key import api_key


def get_api_key(request):
    return {'api_key': api_key}
