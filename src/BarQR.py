from QR_Generator import QR
from Barcode_Generator import Barcode
import sys

class BarQR:
    """
    Abstracts the behavior of QR and Barcode classes allowing either a barcode
    or QR code to be generated and saved
    """

    def __init__(self):
        self._code = None

    def generate(self, data, type):
        if type=='Barcode':
            self._code = Barcode()
            self._code.generate(data)
        elif type=='QR':
            self._code = QR()
            self._code.generate(data)
        else:
            sys.exit('Unknown type of code, BarQR only supports barcodes \
                     and QR codes')

    def savePNG(self, filepath):
        self._code.savePNG(filepath)

    def saveSVG(self, filepath):
        self._code.saveSVG(filepath)

    @property
    def img(self):
        return self._code.img

    @property
    def data(self):
        return self._code.data
