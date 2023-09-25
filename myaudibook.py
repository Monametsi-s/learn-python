import PyPDF2
import pyttsx3

book = open("hold me tight.pdf", "rb")
read = PyPDF2.PdfReader(book)
pages_no = len(read.pages)
print(pages_no)


'''
book = open("hold me tight.pdf", "rb")
read_book = PyPDF2.PdfReader(book)
total_pages = len(read_book.pages)
print(total_pages)'''