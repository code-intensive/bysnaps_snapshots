from abc import abstractmethod

import cv2
from PIL.Image import Image

from snapshots.modules.decoders.interfaces.snap_decoder_interface import ISnapDecoder


class CV2SnapDecoder(ISnapDecoder):
    """CV2 implementation of the SnapDecoder interface."""

    @staticmethod
    @abstractmethod
    def decode_snap(barcode_image: Image) -> str:
        img = cv2.imread(barcode_image)
        decoder = cv2.QRCodeDetector()
        public_url, *_ = decoder.detectAndDecode(img)
        return public_url
