import PyPDF2
import pyttsx3

# Open the PDF file
pdf_file = open('hold me tight.pdf', 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

# Extract text from each page and combine into a single string
text = ''
for page in range(pdf_reader.getNumPages()):
    text += pdf_reader.getPage(page).extractText()

# Create a text-to-speech engine object
engine = pyttsx3.init()

# Set the speech rate and voice
engine.setProperty('rate', 150) # Adjust the value as needed
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # Select the desired voice

# Convert the text to speech and save as an audio file
engine.save_to_file(text, 'example.mp3')
engine.runAndWait()
