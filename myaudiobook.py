import PyPDF2
import pyttsx3

book = open("hold me tight.pdf", "br")
read_book = PyPDF2.PdfReader(book)
total_pages = read_book.pages
print(total_pages)