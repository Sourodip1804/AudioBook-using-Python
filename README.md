# 📖 PDF to Audiobook Converter

A simple Python project that converts the text of a PDF file into **spoken audio** using **Text-to-Speech (TTS)**.

The program allows you to select a PDF file from your computer and automatically reads its pages aloud.

## ✨ Features

* 📄 Select a PDF file using a file picker.
* 📖 Read text from every page of the PDF.
* 🔊 Convert PDF text into speech.
* ▶️ Read the entire PDF page by page.
* 🐍 Built with Python.
* 🖥️ Simple and beginner-friendly project.

## 🛠️ Technologies Used

* **Python**
* **PyPDF2** — Used to read and extract text from PDF files.
* **pyttsx3** — Used for text-to-speech conversion.
* **Tkinter** — Used to open a file-selection dialog.

## 📂 Project Structure

```text
PDF-to-Audiobook/
│
├── audiobook.py
├── README.md
└── requirements.txt
```

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/PDF-to-Audiobook.git
```

Go to the project directory:

```bash
cd PDF-to-Audiobook
```

### 2. Install the required libraries

```bash
pip install pyttsx3 PyPDF2
```

> **Note:** Tkinter is usually included with Python. If it is not available on your system, install the appropriate Tkinter package for your operating system.

## ▶️ How to Run

Run the Python program:

```bash
python audiobook.py
```

A file-selection window will appear.

1. Select the PDF you want to listen to.
2. The program reads the PDF page by page.
3. The extracted text is sent to `pyttsx3`.
4. The text is converted into speech.
5. The program continues until all pages have been read.

## 💻 Example Code

```python
import pyttsx3
import PyPDF2
from tkinter.filedialog import askopenfilename

book = askopenfilename()

pdfreader = PyPDF2.PdfReader(book)
pages = len(pdfreader.pages)

player = pyttsx3.init()

for num in range(pages):
    page = pdfreader.pages[num]
    text = page.extract_text()

    player.say(text)
    player.runAndWait()
```

## ⚠️ Limitations

* The program works best with PDFs containing selectable text.
* Scanned/image-based PDFs may not work because they require OCR.
* The quality of speech depends on the installed system voice.
* Very large PDFs may take some time to process.

## 🔮 Future Improvements

Some possible improvements for this project:

* 🎚️ Add voice, speed, and volume controls.
* ⏯️ Add Play/Pause/Stop buttons.
* 📁 Support multiple PDF files.
* 💾 Save the generated speech as an audio file.
* 🌐 Add support for multiple languages.
* 🔍 Add OCR support for scanned PDFs.
* 🖥️ Create a graphical user interface.

## 🎯 Purpose of the Project

This project was created as a beginner-friendly Python project to practice:

* File handling
* PDF processing
* Python libraries
* Text extraction
* Text-to-Speech
* GUI file selection
* Loops and functions

## 📜 License

This project is open-source and available under the **MIT License**.

---

⭐ If you find this project useful, consider giving the repository a star!
