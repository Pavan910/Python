import pyqrcode
from tkinter import *
from tkinter import messagebox


def generateQR():
    inputString = enterTextField.get()
    scale = enterScaleField.get()
    if len(scale):
       try:
        scale = int(scale)
       except:
        messagebox.showerror("error",
        "scale should be interger value ex: 1,2,3...")
        return
    else:
        scale = 5
    if len(inputString):
        qrcode = pyqrcode.create(inputString)
        savepath = "C:\\Users\\Pavan Singh\Desktop\\" + inputString + "_" + str(scale)
        qrcode.svg(savepath + ".svg", scale=scale)
        qrcode.svg(savepath + ".png", scale=scale)
        messagebox.showinfo('success', "your QR code is generated and save at this path:" + savepath + ".png/.svg")
    else:
        messagebox.showerror("enter", "text field is empty")


def clearAll():
    enterTextField.delete(0, END)
    enterTextField.focus_set()


if __name__ == "__main__":
    window = Tk()
    window.configure(background='light green')
    window.geometry("600x100")
    window.title("QR code generator")
    enterTextLabel = Label(window, text="enter text", fg="black", bg='grey')
    enterTextLabel.grid(row=2, column=1, sticky="E", padx="10", pady="10")
    enterScaleLabel = Label(window, text="enter scale", fg="black", bg='grey')
    enterScaleLabel.grid(row=2, column=4, sticky="E", padx="10", pady="10")
    enterTextField = Entry(window)
    enterTextField.grid(row=2, column=2, sticky="E", padx="60", pady="10")
    enterScaleField = Entry(window)
    enterScaleField.grid(row=2, column=5, sticky="E", pady="10")
    generateButton = Button(window, text="generate", bg="red", fg="black", command=generateQR)
    clearButton = Button(window, text="clear", bg="red", fg="black", command=clearAll)
    generateButton.grid(row=3, column=3)
    clearButton.grid(row=4, column=3, pady="5")
    window.mainloop()
