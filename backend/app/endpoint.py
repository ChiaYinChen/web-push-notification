"""Endpoint."""
from fastapi import APIRouter

from .config import settings
from .schema import Message, NotifyPayload, SubscriptionInfo, Vapid
from .service import send_web_push

router = APIRouter()

# store subscriptions
subscriptions = []


@router.get("/subscribe", response_model=Vapid)
async def get_public_key():
    """Get vapid public key."""
    return Vapid(public_key=settings.VAPID_PUBLIC_KEY)


@router.post("/subscribe", response_model=Message)
async def create_subscribe(subscription: SubscriptionInfo):
    """Store subscription information."""
    if subscription not in subscriptions:
        subscriptions.append(subscription)
    return Message(message="Subscription successful")


@router.post("/notify", response_model=Message)
async def notify(payload: NotifyPayload):
    for subscription in subscriptions:
        await send_web_push(subscription.dict(), payload.dict())
    return Message(message="Notification sent")
