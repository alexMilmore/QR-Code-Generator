from tkinter import BitmapImage
import pyqrcode
import re
import os

class QR:
    """ Stores all functionality for qr code creation """

    def __init__(self):
        self._data = None
        self._qr = None

    def generate(self, data):
        """
        creates new qr code

        data -- data that is to be translated into QR
        """

        self._data = data
        self._qr = pyqrcode.create(self._data)
        self._imageFile = '../images'

    def savePNG(self, filepath):
        # add .png if missing
        filepath = filepath if re.search('.png$', filepath) else filepath + '.png'
        self._qr.png(os.path.join(self._imageFile, filepath))

    def saveSVG(self, filepath):
        # add .svg if missing
        filepath = filepath if re.search('.svg$', filepath) else filepath + '.svg'
        self._qr.svg(os.path.join(self._imageFile, filepath))


    @property
    def img(self):
        return BitmapImage(data=self._qr.xbm(scale=8))

    @property
    def data(self):
        return self._data
