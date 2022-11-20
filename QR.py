from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import qrcode as qr
import cv2


def browse():
    fln = filedialog.askopenfilename()
    img1 = cv2.imread(fln)
    detector = cv2.QRCodeDetector()

    data, bbox, _ = detector.detectAndDecode(img1)

    if bbox is not None:
        readtext = Label(mainwindow, text=data,
                         font=("Courier", 18), fg='black', bd=5, background='plum1')  # subject to generate code
        readtext.grid(row=6, column=0)


def generate():
    global img, svimg
    if len(subject.get()) == 0:
        messagebox.showerror("Enter a subject", "Please Enter a Text / Url")

    else:
        img = qr.make(subject.get())
        messagebox.showinfo("QRCode Generated", "Click on 'SHOW' to View")


def show():
    if len(subject.get()) == 0:
        messagebox.showerror("Enter a subject", "Please Enter a Text / Url")
    else:
        try:
            img.show()
        except:
            pass


def save():
    try:
        if len(fname.get()) != 0:
            path = "/"  # Enter path name to save your qrcode image
            img.save(path+fname.get()+'.png')
            messagebox.showinfo("Image Saved", "Save Successful")
        else:
            messagebox.showerror("Filename is Empty",
                                 "File Name couldn't be Empty")
    except:
        messagebox.showerror("Generate a  QR Code first",
                             " Generate a  QR Code first")


mainwindow = Tk()
mainwindow.title("QR Code Generator")
mainwindow.config(bg='plum1')
mainwindow.geometry("1800x1800")

Name = Label(mainwindow, text="QR Code Generator ",
             bg='white', fg='blue', font=('forte', 35, 'bold'))
Name.grid(row=0, column=2)

gentext = Label(mainwindow, text="Enter Text / Url etc", font=('italic', 30, 'bold'),
                fg='red', bd=3, bg="plum1")              # subject to generate code of
gentext.grid(row=1, column=0)

btn = Button(mainwindow, text="Select and Decode", bg='purple', fg='black', font=(
    "times 25", 25, 'bold', 'italic'), width=20, command=browse)
btn.grid(row=5, column=0)

subject = StringVar()
genentry = Entry(mainwindow, textvariable=subject, width=30, font="times 20")
genentry.grid(row=1, column=3)

filename = Label(mainwindow, text="File Name To Save", font=(
    'italic', 30, 'bold'), fg='red', bd=3, bg="plum1")        # filename for saving
filename.grid(row=3, column=0)

fname = StringVar()
fentry = Entry(mainwindow, textvariable=fname, width=30, font="times 20")
fentry.grid(row=3, column=3)

genb = Button(mainwindow, text="Generate",  bg='silver', fg='darkolivegreen4', activebackground='blue',
              width=10, activeforeground='yellow', font=("times 20", 25, 'bold', 'italic'), command=generate)    # Creating "save as" and "generate" buttons
genb.grid(row=5, column=2)

savb = Button(mainwindow, text="Save", bg='orange', width=10, command=save,
              font=("times 20", 25, 'bold', 'italic'))
savb.grid(row=5, column=3)

resetApp = Button(mainwindow, text='Show', bg='black', fg='white', font=(
    "times 20", 25, 'bold', 'italic'), width=10, command=show)
resetApp.grid(row=6, column=3)

# Placing QR Code into the main window
image = Label(mainwindow)
image.grid(row=6, column=2)

btn2 = Button(mainwindow, text="Exit", bg='black', fg='white', font=(
    "times 20", 25, 'bold', 'italic'), width=10, command=lambda: exit())
btn2.grid(row=6, column=2)

rows = 7
columns = 4

for row in range(rows+1):
    mainwindow.grid_rowconfigure(row, weight=1)

for column in range(columns+1):
    mainwindow.grid_columnconfigure(column, weight=1)

mainwindow.mainloop()
