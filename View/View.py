from Controller import ShiftController
from Controller import AffineController
from Controller import VignenereController
from Controller import HillController
from Model import DAO
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math


class View:
    def __init__(self):
        self.main = Tk()
        self.main.title("Multi-encryptor")
        self.icon = PhotoImage(file="Image/shield.png")
        self.main.iconphoto(False, self.icon)
        self.main.attributes("-topmost", True)
        self.main.resizable(False, False)

        self.MainFrame = Frame(self.main)

        self.MainFrame.pack(fill="both", expand=1)

        self.TextLabel = Label(self.MainFrame, text="Bản rõ:", font=("Arial", "12"))
        self.TextField = Text(self.MainFrame, borderwidth=2, relief="ridge", width=60, height=10)
        self.TextScrollbar = Scrollbar(self.MainFrame, command=self.TextField.yview, orient=VERTICAL)
        self.TextField['yscrollcommand'] = self.TextScrollbar.set

        self.CryptLabel = Label(self.MainFrame, text="Bản mã:", font=("Arial", "12"))
        self.CryptField = Text(self.MainFrame, borderwidth=2, relief="ridge", width=60, height=10)
        self.CryptScrollbar = Scrollbar(self.MainFrame, command=self.CryptField.yview, orient=VERTICAL)
        self.CryptField['yscrollcommand'] = self.CryptScrollbar.set

        self.CipherOptionLabel = Label(self.MainFrame, text="Hệ mã hóa", font=("Arial", "14", "bold"))
        self.option = ["Shift Cipher", "Affine Cipher", "Vignenere Cipher", "Hill Cipher"]
        self.CipherOption = ttk.Combobox(self.MainFrame, values=self.option, state='readonly')
        self.CipherOption.current(0)

        self.KLabel = Label(self.MainFrame, text="Hệ số k:", font=("Arial", "12"))
        self.KField = Entry(self.MainFrame, font=("Arial", "12"))

        self.EncryptButton = ttk.Button(self.MainFrame, text="Encrypt", command=self.EncryptButtonClick)
        self.DecryptButton = ttk.Button(self.MainFrame, text="Decrypt", command=self.DecryptButtonClick)

        self.MainFrame.grid(column=0, row=0)

        self.TextLabel.grid(column=0, row=0, sticky=W)
        self.TextField.grid(column=0, row=1, columnspan=2, rowspan=2)
        self.TextScrollbar.grid(column=2, row=1, rowspan=2, sticky=W + N + S)

        self.CryptLabel.grid(column=0, row=3, sticky=W)
        self.CryptField.grid(column=0, row=4, columnspan=2, rowspan=2)
        self.CryptScrollbar.grid(column=2, row=4, rowspan=2, sticky=W + N + S)

        self.CipherOptionLabel.grid(column=3, row=1, columnspan=2, padx=10)
        self.CipherOption.grid(column=3, row=2, columnspan=2)

        self.KLabel.grid(column=3, row=3, sticky=W, padx=10)
        self.KField.grid(column=3, row=4, columnspan=2, sticky=N, padx=10)

        self.EncryptButton.grid(column=3, row=5, sticky=S)
        self.DecryptButton.grid(column=4, row=5, sticky=S)

        self.main.mainloop()

    def EncryptButtonClick(self):
        s = self.TextField.get('1.0', 'end-1c')
        k = self.KField.get()
        if s == "":
            self.ShowText()
        else:
            DAO.SetText(s)
            if k == "":
                messagebox.showinfo("Hệ số k", "Chưa điền hệ số k!")
            else:
                crypt = ""
                if self.CipherOption.get() == "Shift Cipher":
                    try:
                        k = int(k)
                        crypt = ShiftController.Encrypt(k)
                    except ValueError:
                        messagebox.showinfo("Hệ số k", "Hệ số k sai định dạng!")
                elif self.CipherOption.get() == "Affine Cipher":
                    k = tuple(int(num) for num in
                              k.replace(", ", ",").replace("(", "").replace(")", "")
                              .replace("[", "").replace("]", "").replace("{", "")
                              .replace("}", "").split(","))
                    if len(k) != 2:
                        messagebox.showinfo("Hệ số k", "Hệ số k sai định dạng!")
                    elif math.gcd(k[0], 95) != 1:
                        messagebox.showinfo("Hệ số k", "Hệ số k không hợp lệ!")
                    else:
                        crypt = AffineController.Encrypt(k)
                elif self.CipherOption.get() == "Vignenere Cipher":
                    try:
                        k = int(k)
                        crypt = VignenereController.Encrypt(k)
                    except ValueError:
                        messagebox.showinfo("Hệ số k", "Hệ số k sai định dạng!")
                elif self.CipherOption.get() == "Hill Cipher":
                    try:
                        k = int(k)
                        crypt = HillController.Encrypt(k)
                    except ValueError:
                        messagebox.showinfo("Hệ số k", "Hệ số k sai định dạng!")
                self.CryptField.delete('1.0', 'end-1c')
                self.CryptField.insert(END, crypt)
                DAO.SetCrypt(crypt)

    def DecryptButtonClick(self):
        s = self.CryptField.get('1.0', 'end-1c')
        k = self.KField.get()
        if s == "":
            self.ShowCrypt()
        else:
            DAO.SetCrypt(s)
            if k == "":
                messagebox.showinfo("Hệ số k", "Chưa điền hệ số k!")
            else:
                text = ""
                if self.CipherOption.get() == "Shift Cipher":
                    try:
                        k = int(k)
                        text = ShiftController.Decrypt(k)
                    except ValueError:
                        messagebox.showinfo("Hệ số k", "Hệ số k sai định dạng!")
                elif self.CipherOption.get() == "Affine Cipher":
                    k = tuple(int(num) for num in
                              k.replace(", ", ",").replace("(", "").replace(")", "")
                              .replace("[", "").replace("]", "").replace("{", "")
                              .replace("}", "").split(","))
                    if len(k) != 2:
                        messagebox.showinfo("Hệ số k", "Hệ số k sai định dạng!")
                    elif math.gcd(k[0], 95) != 1:
                        messagebox.showinfo("Hệ số k", "Hệ số k không hợp lệ!")
                    else:
                        text = AffineController.Decrypt(k)
                elif self.CipherOption.get() == "Vignenere Cipher":
                    try:
                        k = int(k)
                        text = VignenereController.Decrypt(k)
                    except ValueError:
                        messagebox.showinfo("Hệ số k", "Hệ số k sai định dạng!")
                elif self.CipherOption.get() == "Hill Cipher":
                    try:
                        k = int(k)
                        text = HillController.Decrypt(k)
                    except ValueError:
                        messagebox.showinfo("Hệ số k", "Hệ số k sai định dạng!")
                self.TextField.delete('1.0', 'end-1c')
                self.TextField.insert(END, text)
                DAO.SetText(text)

    def ShowText(self):
        self.TextField.insert(END, DAO.GetText())

    def ShowCrypt(self):
        self.CryptField.insert(END, DAO.GetCrypt())
