import cv2
from models.snap_datas import SnapData
from modules.decoders.interfaces.snap_decoder_interface import ISnapDecoder
from PIL.Image import Image


class CV2SnapDecoder(ISnapDecoder):
    @classmethod
    def decode_snap(cls, barcode_image: Image) -> SnapData:
        img = cv2.imread(barcode_image)
        decoder = cv2.QRCodeDetector()
        snap_data, _, _ = decoder.detectAndDecode(img)
        return snap_data
