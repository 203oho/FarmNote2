import qrcode
import io

def generate_qr_code(data: str) -> io.BytesIO:
    """
    Generate a QR code as a PNG image.

    Args:
        data (str): The data to encode in the QR code.

    Returns:
        io.BytesIO: A BytesIO stream containing the QR code image.
    """
    qr = qrcode.make(data)
    buffer = io.BytesIO()
    qr.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer