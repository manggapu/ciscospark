import re


# Common Functions
def _sparkurl(path):
    return 'https://api.ciscospark.com/v1' + path


def _sparktoken(token):
    token_prefix = 'Bearer '
    if not re.match(token_prefix, token):
        return 'Bearer ' + token
    else:
        return token
