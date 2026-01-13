import cv2
import re
from pyzbar.pyzbar import decode


def process_image(image_path: str) -> str | None:
    """
    Processa uma imagem de CT-e e retorna a chave de acesso (44 dígitos).
    Retorna None se não encontrar uma chave válida.
    """

    # Carrega a imagem
    image = cv2.imread(image_path)
    if image is None:
        return None

    # Converte para tons de cinza
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detecta códigos de barras
    barcodes = decode(gray)

    # Padrão da chave CT-e (44 dígitos)
    cte_pattern = re.compile(
        r"(11|12|13|14|15|16|17|21|22|23|24|25|26|27|28|29|31|32|33|35|41|42|43|50|51|52|53|99)\d{42}"
    )

    for barcode in barcodes:
        data = barcode.data.decode("utf-8")

        # Ignora QR Code
        if barcode.type == "QRCODE":
            continue

        match = cte_pattern.search(data)
        if match:
            return match.group()

    return None
