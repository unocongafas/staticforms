"""Form."""
from starlette.background import BackgroundTasks
from starlette.responses import RedirectResponse

from .. import settings
from .. import tasks
from ..helpers import prepare_text


async def post(request):
    """Handle form request."""
    data = dict(request.state.payload)

    if data.pop('_honey', None):
        return

    config = {
        'meta': {
            'form': data.pop('_form', None),
            'user_id': data.pop('_user_id', None),
            'user_ip': request.headers.get('X-Real-Ip'),
            'user_agent': request.headers.get('User-Agent'),
            'referer': data.pop('_referer', request.headers.get('Referer')),
            'redirect': data.pop('_redirect', settings.DEFAULT_REDIRECT),
            'webhook': data.pop('_webhook', settings.DEFAULT_WEBHOOK)
        },
        'email': {
            'from': settings.SMTP_FROM,
            'to': data.pop('_to', settings.DEFAULT_TO),
            'reply_to': data.pop('_reply_to', data.get('email')),
            'cc': data.pop('_cc', settings.DEFAULT_CC),
            'bcc': data.pop('_bcc', settings.DEFAULT_BCC),
            'subject': data.pop('_subject', settings.DEFAULT_SUBJECT),
            'text': prepare_text(data)
        },
        'data': data
    }

    background = BackgroundTasks()
    background.add_task(tasks.send_email, config=config)
    background.add_task(tasks.send_webhook, config=config)

    return RedirectResponse(config['meta']['redirect'], 303,  background=background)
