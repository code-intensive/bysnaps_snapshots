from abc import ABCMeta, abstractmethod

from PIL import Image


class ISnapDecoder(metaclass=ABCMeta):
    """Snap decoder interface."""

    @staticmethod
    @abstractmethod
    def decode_snap(barcode_image: Image) -> str:
        """Decodes a barcode.

        :param barcode_image: the image to be decoded.

        :return: The public url to the snapshot.

        :rtype: str.
        """
