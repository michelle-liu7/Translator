from googletrans import Translator
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import os


# translator = Translator()
# text = "Coronavirus disease 2019 (COVID-19), also known as the coronavirus or COVID, is a contagious disease caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). The first known case was identified in Wuhan, China, in December 2019. The disease has since spread worldwide, leading to an ongoing pandemic."

# print(translator.translate(text, dest='zh-cn').text)

LANGUAGE_CODE = {"Chinese(simplified)":"zh-cn", "Chinese(traditional)":"zh-tw", "Hindi":"hi", "Spanish":"es", "French":"fr","Arabic":"ar"}
directory = ""

def openFile():
    """
    lets user pick an input txt file and display its contents in inputBox
    """
    txtFile = filedialog.askopenfilename(
        initialdir= "./",
        title = "Open a file",
        filetypes=(("text files", "*.txt"),)
    )
    if txtFile != "":
        global directory
        directory = os.path.split(txtFile)[0]
        txtFile = open(txtFile, "r")
        data = txtFile.read()
        # print(data)
        inputBox.delete(1.0, END)
        inputBox.insert(END, data)
        txtFile.close()

def writeFile(data):
    """
    writes data to output.txt in the directory of the input file
    """
    if directory != "":        
        f = open(os.path.join(directory, "output.txt"), "w")
        f.write(data)
        f.close()


def translate():
    """
    translates English text into a chosen language and displays translation in outputBox
    """
    if (languages.get() != "select a language") and (not inputBox.get(1.0, END).isspace()):
        translator = Translator()
        translation = translator.translate(text=inputBox.get(1.0, END),dest=LANGUAGE_CODE[languages.get()]).text
        outputBox.delete(1.0, END)
        outputBox.insert(END, translation)
        writeFile(translation)
    else:
        outputBox.delete(1.0, END)

# create display window 
root = Tk()
root.geometry('1080x500')
root.resizable(0,0) # cannot resize window
root.config(bg="white smoke")
root.title("Transformatin Service - Translator")

# title
Label(root, text= "English Text Translator", font="Calibri 22 bold", bg="white smoke", pady=5).pack()

# select file
Label(root, text="Please select a file to read input from", font="Calibri 14 bold", bg="white smoke").place(x=20, y=45)
Button(root, text="select file", command=openFile).place(x=20, y=70)
Label(root, text="* txt files only", font="Calibri", bg="white smoke").place(x=100, y=70)

# input box
Label(root, text="Input", font="Calibri 14 bold", bg="white smoke").place(x=20, y=100)
inputBox = Text(root, height = 20, width = 60, wrap = WORD)
inputBox.place(x=20,y=125)

# output language dropdown and translate button
Label(root, text="Output language", font="Calibri 14 bold", bg="white smoke").place(x=480, y=170)
dropdownOpt = ['Chinese(simplified)', 'Chinese(traditional)', 'Hindi', 'Spanish', 'French', 'Arabic']
languages = ttk.Combobox(root, values = dropdownOpt, width=13, state="readonly")
languages.place(x=470,y=200)
languages.set("select a language")
Button(root, text="Translate", command=translate).place(x=510, y=240)

# output box
Label(root, text="Output", font="Calibri 14 bold", bg="white smoke").place(x=630, y=100)
outputBox = Text(root, height = 20, width = 60, wrap = WORD)
outputBox.place(x=630,y=125)

root.mainloop()
