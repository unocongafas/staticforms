"""Prepare text."""
from .. import settings


def prepare_text(data):
    """Prepare message."""
    return "\n".join((
        f"{settings.FRIENDLY_NAMES.get(key, key)}: {data[key]}"
        for key in data
    ))
