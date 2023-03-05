"""Service."""
import json
import logging

from pywebpush import WebPushException, webpush

from .config import settings

logger = logging.getLogger(__name__)


async def send_web_push(
    subscription_information: dict,
    message_body: dict
) -> bool:
    """Send a webpush message."""
    try:
        webpush(
            subscription_info=subscription_information,
            data=json.dumps(message_body),
            vapid_private_key=settings.VAPID_PRIVATE_KEY,
            vapid_claims=settings.VAPID_CLAIMS,
        )
        return True
    except WebPushException as exc:
        logger.error("Exception while trying to send push notification")
        # Mozilla returns additional information in the body of the response.
        if exc.response and exc.response.json():
            logger.error(exc.response.json())
        return False
