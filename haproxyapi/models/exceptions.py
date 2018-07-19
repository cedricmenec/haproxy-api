class HapiError(Exception):
    """
    Basic HaProxy API Exception
    """
    # Default HTTP Status code is 500
    status_code = 500
