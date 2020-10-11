"""Send webhook."""
import httpx


async def send_webhook(config):
    """Send webhook."""
    webhook = config.get('meta', {}).get('webhook')

    if not webhook:
        return

    async with httpx.AsyncClient() as client:
        await client.post(webhook, json=config['data'])
