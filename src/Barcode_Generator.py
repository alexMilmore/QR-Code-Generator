from tkinter import PhotoImage
import barcode
from barcode.writer import ImageWriter
import re
import numpy as np
from PIL import ImageTk
import os

class Barcode:
    """ Stores all functionality for qr code creation """

    def __init__(self):
        self._data = None;
        self._barcode = None;

    def generate(self, data):
        """
        creates new barcode

        data -- data that is to be translated into a barcode
        """

        self._data = data;
        self._codeType = 'code128'
        self._imageFile = 'images'

    def savePNG(self, filepath):
        # add .png if missing
        filepath = filepath[:-4] if re.search('.png$', filepath) else filepath
        bar = barcode.get(self._codeType, self._data, writer=ImageWriter())
        bar.save(os.path.join(self._imageFile,filepath))

    def saveSVG(self, filepath):
        # remove .svg from end
        filepath = filepath[:-4] if re.search('.svg$', filepath) else filepath
        bar = barcode.get(self._codeType, self._data)
        bar.save(os.path.join(self._imageFile, filepath))

    @property
    def img(self):
        code =  barcode.get(self._codeType, self._data, writer=ImageWriter(mode='RGBA'))
        image = code.render();
        return ImageTk.PhotoImage(image);

    @property
    def data(self):
        return self._data
