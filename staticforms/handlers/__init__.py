"""Handlers."""
from starlette.routing import Route

from . import ping, form

routes = [
    Route('/ping', ping.get, methods=['GET']),
    Route('/form', form.post, methods=['POST']),
]
