"""Static forms."""
from starlette.applications import Starlette

from .middlewares import middleware
from .handlers import routes

app = Starlette(routes=routes, middleware=middleware)
