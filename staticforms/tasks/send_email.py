"""Send email."""
from email.message import EmailMessage

import aiosmtplib

from .. import settings

HEADERS = (
    'From',
    'To',
    'Reply-To',
    'CC',
    'BCC',
    'Subject'
)


async def send_email(config):
    """Send email."""
    message = EmailMessage()

    for header in HEADERS:
        key = header.lower().replace('-', '_')
        if config['email'].get(key):
            message[header] = config['email'][key]

    message.set_content(config['email']['text'])

    await aiosmtplib.send(
        message,
        hostname=settings.SMTP_HOST,
        port=settings.SMTP_PORT,
        username=settings.SMTP_USER,
        password=settings.SMTP_PASS,
        use_tls=settings.SMTP_USETLS,
        start_tls=settings.SMTP_STARTTLS
    )
