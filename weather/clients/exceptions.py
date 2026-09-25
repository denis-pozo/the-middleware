class CountryClientException(Exception):
    """Base for all countries-client errors."""

class CountryNotFoundException(CountryClientException):
    """Upstream returned 404 — unknown country."""

class CountryServiceException(CountryClientException):
    """Upstream unreachable, timed out, or returned 5xx/malformed response."""