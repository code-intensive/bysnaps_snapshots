from io import BytesIO

from qrcode import make


class QRCodeGeneratorService:
    """QRcode generator for creating snapshots."""

    @staticmethod
    def generate_snap(id: str, **options: dict[str, str | int]) -> bytes:
        temp_file = BytesIO()
        qr_image = make(id, **options)
        qr_image.save(temp_file)
        temp_file.seek(0)
        return temp_file.getvalue()
