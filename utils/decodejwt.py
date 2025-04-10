import base64
import json


def add_padding(base64_string):
    """Add padding to a Base64URL string if necessary."""
    return base64_string + "=" * (-len(base64_string) % 4)


def decode_jwt(jwt_token):
    """Decode a JWT token into header, payload, and signature."""
    if not jwt_token:
        raise ValueError("JWT token is None or empty")

    parts = jwt_token.split(".")

    if len(parts) < 2 or len(parts) > 3:
        raise ValueError(
            "Invalid JWT structure. A JWT must have two or three parts separated by dots."
        )

    try:
        header = base64.urlsafe_b64decode(add_padding(parts[0])).decode("utf-8")
        decoded_header = json.loads(header)

        alg = decoded_header.get("alg", None)
        if not alg:
            print(
                "Warning: No 'alg' (algorithm) field found in the header. This JWT might be unsigned."
            )

        payload = base64.urlsafe_b64decode(add_padding(parts[1])).decode("utf-8")
        decoded_payload = json.loads(payload)

        signature = None
        if len(parts) == 3:
            signature = base64.urlsafe_b64decode(add_padding(parts[2])).hex()

        return decoded_header, decoded_payload, signature
    except Exception as e:
        raise ValueError(f"Failed to decode JWT: {e}")
