'''
tips for using PyPDF2 version 3.0.1
from PyPDF2 import PdfReader

reading_pdf = PdfReader("example.pdf") 
number_of_pages = len(reading_pdf.pages)
page = reader.pages[0]
page = reading_pdf.pages[0]
extracting_text = page.extract_text()

more info at https://code.tutsplus.com/how-
            to-work-with-pdf-documents-using-
            python--cms-25726t'''

import re
import pyttsx3
import PyPDF2

def remove_emojis(string):
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F" # emoticons
        u"\U0001F300-\U0001F5FF" # symbols & pictographs
        u"\U0001F680-\U0001F6FF" # transport & map symbols
        u"\U0001F1E0-\U0001F1FF" # flags (iOS)
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        "]+", 
        flags=re.UNICODE
    )
    return emoji_pattern.sub(r'', string)

speaker = pyttsx3.init()
book = open("hold me tight.pdf", "rb")
read = PyPDF2.PdfReader(book)
pages_no = len(read.pages)

full_text = ""
for page_no in range(pages_no):
    page = read.pages[page_no]
    text = page.extract_text()
    full_text += text

full_text = remove_emojis(full_text)
print(full_text)
speaker.save_to_file(full_text, "audibook.mp3")
speaker.runAndWait()

speaker.stop()