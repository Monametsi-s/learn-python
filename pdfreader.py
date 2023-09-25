'''import PyPDF2
import pyttsx3

pdfReader = PyPDF2.PdfFileReader(open('hold me tight.pdf', 'rb'))
speaker = pyttsx3.init()

for page_num in range(pdfReader.numPages):
    text =  pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()

engine.save_to_file(text, 'audio.mp3')
engine.runAndWait()'''
import PyPDF2
import pyttsx3

# Initialize the Text-to-Speech engine
speaker = pyttsx3.init()

# Open the PDF file
pdf_file = 'hold me tight.pdf'
pdfReader = PyPDF2.PdfReader(open(pdf_file, 'rb'))

# Create an empty string to store the entire text from the PDF
full_text = ""

for page_num in range(len(pdfReader.pages)):
    page = pdfReader.pages[page_num]
    text = page.extract_text()
    full_text += text

# Convert the full text to audio
speaker.save_to_file(full_text, 'audio.mp3')
speaker.runAndWait()

# Stop the speaker after processing
speaker.stop()

print("Audiobook saved as 'audio.mp3'")
