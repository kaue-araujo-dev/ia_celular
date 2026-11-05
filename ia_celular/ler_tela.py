
import pytesseract
from PIL import Image

# Informa ao Python onde está o Tesseract
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# Abre a captura de tela
imagem = Image.open("tela.png")

# Lê o texto da imagem
texto = pytesseract.image_to_string(imagem, lang="por")

print("===== TEXTO RECONHECIDO =====")
print(texto)
