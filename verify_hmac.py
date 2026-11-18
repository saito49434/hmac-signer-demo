import hashlib
import hmac

def sign(secret: bytes, payload: bytes) -> str:
    return hmac.new(secret, payload, hashlib.sha256).hexdigest()

def verify(secret: bytes, payload: bytes, sig: str) -> bool:
    return hmac.compare_digest(sign(secret, payload), sig)
