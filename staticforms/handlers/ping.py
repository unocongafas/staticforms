"""Ping."""
from starlette.responses import UJSONResponse


async def get(request):
    """Handle ping request."""
    return UJSONResponse({'pong': True})
