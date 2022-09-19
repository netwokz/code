from http.client import HTTPConnection
from operator import truediv
from urllib.parse import urlparse

def site_is_online(url, timout=2):
    """Return True if the target URL is online.

    Raise an exception otherwise.
    """
    error = Exception("unknown error")
    parser = urlparse(url)
    host = parser.netloc or parser.path.split("/")[0]
    for port in (80,443):
        connection = HTTPConnection(host=host, port=port, timeout=timout)
        try:
            connection.request("HEAD", "/")
            return True
        except Exception as e:
            error =e
        finally:
            connection.close()
    raise error