from googletrans import Translator
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import os
import json


# translator = Translator()
# text = "Coronavirus disease 2019 (COVID-19), also known as the coronavirus or COVID, is a contagious disease caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). The first known case was identified in Wuhan, China, in December 2019. The disease has since spread worldwide, leading to an ongoing pandemic."

# print(translator.translate(text, dest='zh-cn').text)

LANGUAGE_CODE = {"Chinese(simplified)":"zh-cn", "Chinese(traditional)":"zh-tw", "Hindi":"hi", "Spanish":"es", "French":"fr","Arabic":"ar"}
DEFAULT_DIR = "C:/OSU/CS361/WebScrapper"

def openFile():
    """
    lets user pick an input json file and display its contents in inputBox
    """
    global DEFAULT_DIR

    jsonFile = filedialog.askopenfilename(
        initialdir= DEFAULT_DIR,
        title = "Open a file",
        filetypes=(("json files", "*.json"),)
    )
    if jsonFile != "":
        jsonFile = open(jsonFile, "r")
        data = json.load(jsonFile)
        # print(data)
        inputBox.delete(1.0, END)
        inputBox.insert(END, data["summary"])
        languages.set(data["language"])
        jsonFile.close()

def writeFile(data):
    """
    writes data to output.txt in the directory of the input file
    """
    global DEFAULT_DIR        
    f = open(DEFAULT_DIR+"/output.txt", "w", encoding="utf-8")
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

def clearBoxes():
    msgBox = messagebox.askquestion("Questions", "Are you sure you want to clear input?")
    if msgBox == "yes":
        inputBox.delete(1.0, END)
        outputBox.delete(1.0, END)

# create display window 
root = Tk()
root.geometry('1080x500')
root.resizable(0,0) # cannot resize window
root.config(bg="white smoke")
root.title("Transformation Service - Translator")

# title
Label(root, text= "English Text Translator", font="Calibri 22 bold", bg="white smoke", pady=5).pack()

# select file
Label(root, text="Please select a file to read input from", font="Calibri 14 bold", bg="white smoke").place(x=20, y=45)
Button(root, text="select file", command=openFile).place(x=20, y=70)
Label(root, text="* json files only", font="Calibri", bg="white smoke").place(x=100, y=70)

# input box
Label(root, text="Input", font="Calibri 14 bold", bg="white smoke").place(x=20, y=100)
inputBox = Text(root, height = 20, width = 50, wrap = WORD)
inputBox.place(x=20,y=125)

# output language dropdown and translate button
Label(root, text="Output language", font="Calibri 14 bold", bg="white smoke").place(x=470, y=170)
dropdownOpt = ['Chinese(simplified)', 'Chinese(traditional)', 'Hindi', 'Spanish', 'French', 'Arabic']
languages = ttk.Combobox(root, values = dropdownOpt, width=13, state="readonly")
languages.place(x=490,y=200)
languages.set("select a language")
Button(root, text="Translate", command=translate).place(x=510, y=240)

# clear button
Button(root, text="Clear", command=clearBoxes).place(x=520, y=290)

# output box
Label(root, text="Output", font="Calibri 14 bold", bg="white smoke").place(x=630, y=100)
outputBox = Text(root, height = 20, width = 50, wrap = WORD)
outputBox.place(x=630,y=125)

# check if input file exists 
if "input.json" in os.listdir(DEFAULT_DIR):
    f = open(DEFAULT_DIR+"/input.json", "r")
    data = json.load(f)
    f.close()
    inputBox.insert(END, data["summary"])
    languages.set(data["language"])
    translate()

root.mainloop()
