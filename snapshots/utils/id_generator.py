from uuid import uuid4


def generate_uuid(prefix: str) -> str:
    """Generates a uuid with a prefix.

    :param prefix: string to be prepended to the
    generated uuid's hexadecimal representation.

    :return: UUID's hexadecimal representation with prefix.

    :rtype: str.
    """
    return f"{ prefix }_{ uuid4().hex }"
