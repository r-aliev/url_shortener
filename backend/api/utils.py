import random
import string

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

from .exceptions import URLIsNotValid


def get_shorten_url(request, original_url: str) -> str:
    # Validate url
    validate = URLValidator()
    try:
        validate(original_url)
    except ValidationError:
        raise URLIsNotValid("Url is not valid")

    # Generate random hash
    random_hash = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
    # Adding the generated hash to the end of host url
    shortened_url = request.build_absolute_uri("/" + random_hash)
    return shortened_url
