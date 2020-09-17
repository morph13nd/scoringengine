from requests import get

def http_status(url: str, status_codes: [int]):
    """
    Check whether the url returns one of the given status codes
    """
    try:
        code = get(f"http://{url}", timeout=1).status_code
        return code in status_codes
    except:
        return False

def http_contains(url: str, keywords: [str], case_sensitive=True):
    """
    Returns true upon finding the keyword in the given page
    """
    pass
