from uuid import uuid4


def generate_uuid(prefix: str) -> str:
    return f"{ prefix }_{ uuid4().hex }"
