from tkinter import *
import os
from BarQR import BarQR

class Application:
    class EntryWithButton:
        row = 0;

        """
        Creates a labelled input field with a button

        row -- the row the gui is displayer
        tkWindow -- the tkinter window to display to
        label -- text label for this set of widgets
        buttons -- dictionary relating button labels and their funcitons
        """
        def __init__(self, row, tkWindow, label, buttons):
            self.data = StringVar()

            self.label = Label(tkWindow, text=label)
            self.label.grid(row=row, column=0, sticky=N+S+E+W)

            self.entry = Entry(tkWindow, textvariable=self.data)
            self.entry.grid(row=row, column=1, sticky=N+S+E+W)

            offset = 0
            for key, val in buttons.items():
                genB = Button(tkWindow, text=key, width=15, command=val)
                genB.grid(row=row,column=3+offset,sticky=N+S+W+E)
                offset += 1

            self.row += 1

    #TODO better variable name than qr
    def updateImg(self, qr, data, type):
        qr.generate(data, type)
        # this needs to be in a variable because otherwise tk makes it invisibe
        self.tkImage = qr.img
        self.imageLabel.config(image = self.tkImage)
        self.subLabel.config(text=type + " of " + qr.data)

    def __init__(self):
        window = Tk()
        window.title("QR Code Generator")

        # qr and bar code generator
        barQR = BarQR()

        # Controls
        qrGen = self.EntryWithButton(0, window, 'Data',
            {'Gen QR':lambda:self.updateImg(barQR, qrGen.data.get(), 'QR'),
            'Gen Barcode':lambda:self.updateImg(barQR, qrGen.data.get(), 'Barcode')})
        qrSave = self.EntryWithButton(1, window, 'Save',
            {'SavePNG':lambda:barQR.savePNG(qrSave.data.get()),
            'SaveSVG':lambda:barQR.saveSVG(qrSave.data.get()), })

        # QR code view
        self.imageLabel = Label(window)
        self.imageLabel.grid(row =2,column =1,sticky=N+S+W+E)

        self.subLabel = Label(window,text="")
        self.subLabel.grid(row =3,column =1,sticky=N+S+W+E)

        #making this resposnsive
        Rows = 4
        Columns = 4

        for row in range(Rows+1):
            window.grid_rowconfigure(row,weight=1)

        for col in range(Columns+1):
            window.grid_columnconfigure(col,weight=1)

        window.mainloop()

if __name__=='__main__':
    Application();
