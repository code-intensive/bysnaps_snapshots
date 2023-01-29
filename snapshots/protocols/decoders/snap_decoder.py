from typing import Protocol

from PIL import Image


class SnapDecoderProtocol(Protocol):
    """Snap decoder protocol."""

    @staticmethod
    def decode_snap(barcode_image: Image) -> str:
        """Decodes a barcode.

        :param barcode_image: the image to be decoded.

        :return: The public url to the snapshot.

        :rtype: str.
        """
