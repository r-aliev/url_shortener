"""URL shortener exception subclasses"""


class URLShortenerError(Exception):
    """Base class for URL shortener exceptions."""
    pass


class URLIsNotValid(URLShortenerError):
    """URL Shortener related exception."""
    pass