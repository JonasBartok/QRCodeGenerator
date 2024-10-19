import qrcode
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class QR:
    def __init__(self, data, filename):
        self.data = data
        self.filename = filename

    def generate(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(self.filename)

    def show(self):
        img = mpimg.imread(self.filename)
        plt.imshow(img, cmap='gray')
        plt.show()


if __name__ == "__main__":
    adress = input("Zadejte adresu: ")
    filename = input("Zadejte název souboru: ")
    if not filename.endswith(".png"):
        filename += ".png"
    qr = QR(adress, filename)
    qr.generate()
    qr.show()