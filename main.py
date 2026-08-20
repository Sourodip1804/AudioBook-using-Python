####### updated code is written 

import pyttsx3 
# for he pyttsx3 library is a powerful, open-source tool used for Text-to-Speech (TTS) conversion in Python.
import PyPDF2
# PyPDF2 is a Python library used to read, write, and modify PDF files.
from tkinter.filedialog import askopenfilename
#tkinter.filedialog is a Python module used to create file-selection windows (file picker dialogs).
#asking the book or the file name from the user
book = askopenfilename()
pdfreader = PyPDF2.PdfReader(book)
pages = len(pdfreader.pages)

# for reading the pages of the book 
for num in range(0, pages):
    page = pdfreader.pages[num]
    # extracting the text from the variable 
    text = page.extract_text()
    # for playing the audio book 
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()
    #
