"""Prepare request."""
from starlette.middleware.base import BaseHTTPMiddleware


class PrepareRequestMiddleware(BaseHTTPMiddleware):
    """Prepare request."""

    async def dispatch(self, request, call_next):
        """Dispatch."""
        request.state.payload = {}

        content_type = request.headers.get('Content-Type') or ''

        if content_type.startswith('application/json'):
            request.state.payload = await request.json()

        elif content_type.startswith('application/x-www-form-urlencoded'):
            payload = await request.form()
            request.state.payload = {key: payload[key] for key in payload}

        return await call_next(request)
