class CountryClientError(Exception):
    """Base for all countries-client errors."""

class CountryNotFoundError(CountryClientError):
    """Upstream returned 404 — unknown country."""

class CountryServiceError(CountryClientError):
    """Upstream unreachable, timed out, or returned 5xx/malformed response."""