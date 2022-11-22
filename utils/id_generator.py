from uuid import uuid4


def generate_uuid(prefix: str) -> str:
    """
    :param prefix: string to be prepended to the
    generated uuid's hexadecimal representation

    :return: `str`: the UUID's hex representation
    """
    return f"{ prefix }_{ uuid4().hex }"
