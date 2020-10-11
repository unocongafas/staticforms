"""Middlewares."""
from starlette.middleware import Middleware

from .prepare_request import PrepareRequestMiddleware

middleware = [
    Middleware(PrepareRequestMiddleware)
]
