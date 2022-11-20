from io import BytesIO

from qrcode import make

from modules.generators.interfaces.snap_generator_interface import ISnapGenerator


class QRCodeSnapGenerator(ISnapGenerator):
    @staticmethod
    def generate_snap(snap_id: str, **options: dict[str, str | int]) -> bytes:
        temp_file = BytesIO()
        qr_image = make(snap_id, **options)
        qr_image.save(temp_file)
        temp_file.seek(0)
        return temp_file.getvalue()
