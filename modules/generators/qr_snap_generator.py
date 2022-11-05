from io import BytesIO
from typing import Dict, Union

from modules.generators.interfaces.snap_generator_interface import ISnapGenerator
from qrcode import make


class QRCodeSnapGenerator(ISnapGenerator):
    @staticmethod
    def generate_snap(snap_id: str, **options: Dict[str, Union[str, int]]) -> bytes:
        temp_file = BytesIO()
        qr_image = make(snap_id, **options)
        qr_image.save(temp_file)
        temp_file.seek(0)
        return temp_file.getvalue()
