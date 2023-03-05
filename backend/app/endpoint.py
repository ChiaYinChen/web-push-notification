"""Endpoint."""
from fastapi import APIRouter

from .schema import Message, NotifyPayload, SubscriptionInfo
from .service import send_web_push

router = APIRouter()

# store subscriptions
subscriptions = []


@router.post("/subscribe")
async def subscribe(subscription: SubscriptionInfo):
    if subscription not in subscriptions:
        subscriptions.append(subscription)
    return Message(message="Subscription successful")


@router.post("/notify")
async def notify(payload: NotifyPayload):
    for subscription in subscriptions:
        await send_web_push(subscription.dict(), payload.dict())
    return Message(message="Notification sent")
