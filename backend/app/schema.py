"""Schema."""
from typing import Any

from pydantic import BaseModel


class Vapid(BaseModel):
    public_key: str


class Keys(BaseModel):
    p256dh: str
    auth: str


class SubscriptionInfo(BaseModel):
    endpoint: str
    keys: Keys


class NotifyPayload(BaseModel):
    title: str
    description: str


class Message(BaseModel):
    message: Any
