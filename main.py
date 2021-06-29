
import pyttsx3
import PyPDF2
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog

bg = '#D4B8B2'
app = Tk()
app.geometry('300x400')
app.title('AudioBook')

app.config(bg=bg)

path = None

def click():
    global path
    path = filedialog.askopenfilename()
    print(f"Path where your PDF File exists {path}")
    print("Hello! Now You're going to listen our audio book")

def listen():
    page_n = page_num_box.get()
    if path and page_n:
        # initialize speaker
        speaker = pyttsx3.init()
        #  Open the PDF
        book = open(path, 'rb')

        #  Read the PDF
        read_file = PyPDF2.PdfFileReader(book)

        # Choosing the page that we want to read
        page = read_file.getPage(int(page_n))

        # Extract the text from the page
        text = page.extractText()
        speaker.say(text)
        # print the text from the page
        print(text)

        speaker.runAndWait()

image = Image.open('vip.png')
imageresize = image.resize((120,120),Image.ANTIALIAS)
image1 = ImageTk.PhotoImage(imageresize)

logo = Label(app, image=image1,bg=bg)
logo.pack()

title = Label(app, text="Welcome to the AudioBook",bg=bg, font='Comic 15')
title.pack(pady = 10)

page_number = Label(app, text="Enter Page Number of Your PDF", bg=bg)
page_number.pack(pady=(20,0))

page_num_box = Entry(app,bg='#7B94C2')
page_num_box.pack(pady=2)

openPDF = Button(app, text="Open", width=16,bg='#7B94C2', command=click)
openPDF.pack(pady=(20,0))

sayPDF = Button(app, text="Listen",width=16,bg='#7B94C2', command=listen)
sayPDF.pack(pady=(20,0))

app.mainloop()
