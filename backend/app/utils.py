"""Utils."""
import base64

import ecdsa


def base64url_encode(bstring: bytes) -> str:
    """Encodes an unpadded Base64 URL-encoded string per RFC 7515."""
    return base64.urlsafe_b64encode(bstring).decode("utf-8").strip("=")


def generate_vapid_keypair() -> dict[str, str]:
    """Generate a new set of encoded key-pair for VAPID."""
    pk = ecdsa.SigningKey.generate(curve=ecdsa.NIST256p)
    vk = pk.get_verifying_key()
    return {
        "private_key": base64url_encode(pk.to_string()),
        "public_key": base64url_encode("\x04".encode() + vk.to_string())
    }
