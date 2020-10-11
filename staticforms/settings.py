"""Config."""
from starlette.config import Config

config = Config(".env")

DEBUG = config('DEBUG', cast=bool, default=False)

SMTP_HOST = config('SMTP_HOST', cast=str, default='127.0.0.1')
SMTP_PORT = config('SMTP_PORT', cast=int, default=587)
SMTP_USER = config('SMTP_USER', cast=str, default=None)
SMTP_PASS = config('SMTP_PASS', cast=str, default=None)
SMTP_USETLS = config('SMTP_USETLS', cast=bool, default=False)
SMTP_STARTTLS = config('SMTP_STARTTLS', cast=bool, default=True)
SMTP_FROM = config('SMTP_FROM', cast=str, default='admin@localhost')

DEFAULT_TO = config('DEFAULT_TO', cast=str, default=None)
DEFAULT_CC = config('DEFAULT_CC', cast=str, default=None)
DEFAULT_BCC = config('DEFAULT_BCC', cast=str, default=None)
DEFAULT_SUBJECT = config('DEFAULT_SUBJECT', cast=str, default='Nuevo envío')
DEFAULT_REDIRECT = config('DEFAULT_REDIRECT', cast=str, default='/thanks')
DEFAULT_WEBHOOK = config('DEFAULT_WEBHOOK', cast=str, default=None)

FRIENDLY_NAMES = {
    'first_name': 'Nombre',
    'last_name': 'Apellidos',
    'email': 'Correo electrónico',
    'phone': 'Teléfono'
}
