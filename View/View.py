from Controller import ShiftController
from Controller import SubstitutionController
from Controller import AffineController
from Controller import VigenereController
from Controller import HillController
from Controller import PermutationController
from Controller import DESController
from Controller import AESController
from Controller import RSAController
from Model import DAO
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math
import random
import numpy as np


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
        self.CryptField = Text(self.MainFrame, borderwidth=2, relief="ridge", width=60, height=10, state="disabled")
        self.CryptScrollbar = Scrollbar(self.MainFrame, command=self.CryptField.yview, orient=VERTICAL)
        self.CryptField['yscrollcommand'] = self.CryptScrollbar.set

        self.CipherOptionLabel = Label(self.MainFrame, text="Hệ mã hóa", font=("Arial", "14", "bold"))
        self.option = ["Shift Cipher", "Substitution Cipher", "Affine Cipher",
                       "Vigenère Cipher", "Hill Cipher", "Permutation Cipher",
                       "DES", "AES", "RSA"]
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
            self.CryptField.configure(state="normal")
            self.CryptField.delete('1.0', 'end-1c')
            self.CryptField.configure(state="disabled")
        else:
            DAO.SetText(s)
            if k == "":
                k = self.autokey()
            else:
                crypt = ""
                if self.CipherOption.get() == "Shift Cipher":
                    try:
                        k = int(k)
                        crypt = ShiftController.Encrypt(k)
                    except ValueError:
                        messagebox.showinfo("Hệ số k", "Hệ số k sai định dạng!")

                elif self.CipherOption.get() == "Substitution Cipher":
                    try:
                        crypt = SubstitutionController.Encrypt(k)
                    except ValueError:
                        messagebox.showinfo("Hệ số k", "Hệ số k sai định dạng!")

                elif self.CipherOption.get() == "Affine Cipher":
                    try:
                        k = tuple(int(num) for num in
                                  k.replace(", ", ",").replace("(", "").replace(")", "")
                                  .replace("[", "").replace("]", "").replace("{", "")
                                  .replace("}", "").replace(",", " ").split(" "))
                        if len(k) != 2:
                            messagebox.showinfo("Hệ số k", "Hệ số k sai định dạng!")
                        elif math.gcd(k[0], 128) != 1:
                            messagebox.showinfo("Hệ số k", "Hệ số k không hợp lệ!")
                        else:
                            crypt = AffineController.Encrypt(k)
                    except ValueError:
                        messagebox.showinfo("Hệ số k", "Hệ số k sai định dạng!")

                elif self.CipherOption.get() == "Vigenère Cipher":
                    crypt = VigenereController.Encrypt(k)

                elif self.CipherOption.get() == "Hill Cipher":
                    try:
                        k = tuple(int(num) for num in
                                  k.replace(", ", ",").replace("(", "").replace(")", "")
                                  .replace("[", "").replace("]", "").replace("{", "")
                                  .replace("}", "").replace(",", " ").split(" "))
                        if len(k) != math.isqrt(len(k)) ** 2:
                            messagebox.showinfo("Hệ số k", "Hệ số k sai định dạng1!")
                        else:
                            crypt = HillController.Encrypt(k)
                    except ValueError:
                        messagebox.showinfo("Hệ số k", "Hệ số k sai định dạng!")

                elif self.CipherOption.get() == "Permutation Cipher":
                    try:
                        k = tuple(int(num) for num in
                                  k.replace(", ", ",").replace("(", "").replace(")", "")
                                  .replace("[", "").replace("]", "").replace("{", "")
                                  .replace("}", "").replace(",", " ").split(" "))
                        crypt = PermutationController.Encrypt(k)
                    except ValueError:
                        messagebox.showinfo("Hệ số k", "Hệ số k sai định dạng!")

                elif self.CipherOption.get() == "DES":
                    try:
                        crypt = DESController.Encrypt(k)
                    except ValueError:
                        messagebox.showinfo("Hệ số k", "Hệ số k sai định dạng!")

                elif self.CipherOption.get() == "AES":
                    try:
                        crypt = AESController.Encrypt(k)
                    except ValueError:
                        messagebox.showinfo("Hệ số k", "Hệ số k sai định dạng!")

                elif self.CipherOption.get() == "RSA":
                    try:
                        crypt = RSAController.Encrypt(k)
                    except ValueError:
                        messagebox.showinfo("Hệ số k", "Hệ số k sai định dạng!")

                self.CryptField.configure(state="normal")
                crypt = DAO.bin_txt(crypt)
                DAO.SetCrypt(crypt)
                self.CryptField.delete('1.0', 'end-1c')
                self.CryptField.insert(END, crypt.strip())
                self.CryptField.configure(state="disabled")

    def DecryptButtonClick(self):
        self.CryptField.configure(state="normal")
        s = self.CryptField.get('1.0', 'end-1c')
        self.CryptField.configure(state="disabled")
        k = self.KField.get()
        if s == "":
            self.CryptField.configure(state="normal")
            self.ShowCrypt()
            self.CryptField.configure(state="disabled")
            self.TextField.delete('1.0', 'end-1c')
        else:
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

                elif self.CipherOption.get() == "Substitution Cipher":
                    try:
                        text = SubstitutionController.Decrypt(k)
                    except ValueError:
                        messagebox.showinfo("Hệ số k", "Hệ số k sai định dạng!")

                elif self.CipherOption.get() == "Affine Cipher":
                    try:
                        k = tuple(int(num) for num in
                                  k.replace(", ", ",").replace("(", "").replace(")", "")
                                  .replace("[", "").replace("]", "").replace("{", "")
                                  .replace("}", "").replace(",", " ").split(" "))
                        if len(k) != 2:
                            messagebox.showinfo("Hệ số k", "Hệ số k sai định dạng!")
                        elif math.gcd(k[0], 128) != 1:
                            messagebox.showinfo("Hệ số k", "Hệ số k không hợp lệ!")
                        else:
                            text = AffineController.Decrypt(k)
                    except ValueError:
                        messagebox.showinfo("Hệ số k", "Hệ số k sai định dạng!")

                elif self.CipherOption.get() == "Vigenère Cipher":
                    text = VigenereController.Decrypt(k)

                elif self.CipherOption.get() == "Hill Cipher":
                    try:
                        k = tuple(int(num) for num in
                                  k.replace(", ", ",").replace("(", "").replace(")", "")
                                  .replace("[", "").replace("]", "").replace("{", "")
                                  .replace("}", "").replace(",", " ").split(" "))
                        if len(k) != math.isqrt(len(k)) ** 2:
                            messagebox.showinfo("Hệ số k", "Hệ số k sai định dạng!")
                        else:
                            text = HillController.Decrypt(k)
                    except ValueError:
                        messagebox.showinfo("Hệ số k", "Hệ số k sai định dạng!")

                elif self.CipherOption.get() == "Permutation Cipher":
                    try:
                        k = tuple(int(num) for num in
                                  k.replace(", ", ",").replace("(", "").replace(")", "")
                                  .replace("[", "").replace("]", "").replace("{", "")
                                  .replace("}", "").replace(",", " ").split(" "))
                        text = PermutationController.Decrypt(k)
                    except ValueError:
                        messagebox.showinfo("Hệ số k", "Hệ số k sai định dạng!")

                elif self.CipherOption.get() == "DES":
                    try:
                        text = DESController.Decrypt(k)
                    except ValueError:
                        messagebox.showinfo("Hệ số k", "Hệ số k sai định dạng!")

                elif self.CipherOption.get() == "AES":
                    try:
                        text = AESController.Decrypt(k)
                    except ValueError:
                        messagebox.showinfo("Hệ số k", "Hệ số k sai định dạng!")

                elif self.CipherOption.get() == "RSA":
                    try:
                        text = RSAController.Decrypt(k)
                    except ValueError:
                        messagebox.showinfo("Hệ số k", "Hệ số k sai định dạng!")

                text = DAO.bin_txt(text)
                DAO.SetText(text)
                self.TextField.delete('1.0', 'end-1c')
                self.TextField.insert(END, text.strip())

    def ShowText(self):
        self.TextField.insert(END, DAO.GetText().strip())

    def ShowCrypt(self):
        self.CryptField.configure(state="normal")
        self.CryptField.insert(END, DAO.GetCrypt().strip())
        self.CryptField.configure(state="disabled")

    def autokey(self):
        k = ""
        if self.CipherOption.get() == "Shift Cipher":
            k = random.randint(0, 127)
            self.KField.insert(END, str(k))
            return k

        elif self.CipherOption.get() == "Substitution Cipher":
            for i in range(32, 127):
                k += chr(i)
            k = list(k)
            random.shuffle(k)
            k = "".join(k)
            self.KField.insert(END, k)
            return k

        elif self.CipherOption.get() == "Affine Cipher":
            k = 2
            while math.gcd(k, 128) != 1:
                k = random.randint(1, 127)
            k = tuple((k, random.randint(0, 127)))
            self.KField.insert(END, str(k))
            return k

        elif self.CipherOption.get() == "Vigenère Cipher":
            k = ""
            for i in range(random.randint(5, 20)):
                k += chr(random.randint(32, 127))
            self.KField.insert(END, k)
            return k

        elif self.CipherOption.get() == "Hill Cipher":
            k = np.zeros((2, 2))
            while math.gcd(int(round(np.linalg.det(k)) % 128), 128) != 1:
                temp = []
                while len(temp) < 16:
                    temp.append(random.randint(-128, 128))
                k = np.array(temp).reshape((math.isqrt(len(temp)), math.isqrt(len(temp))))
            self.KField.insert(END, str(k.flatten()))
            return k

        elif self.CipherOption.get() == "Permutation Cipher":
            k = [i for i in range(len(DAO.GetText()))]
            random.shuffle(k)
            self.KField.insert(END, str(k))
            return k

        else:
            messagebox.showinfo("Hệ số k", "Chưa điền hệ số k!")
            return k
