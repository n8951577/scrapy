# importing required modules
import PyPDF2

# creating a pdf file object
pdfFileObj = open('sample.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print("The Number of Pages in the document is",pdfReader.numPages)
print("\n")

# creating a page object
pageObj = pdfReader.getPage(0)
pageObj1 = pdfReader.getPage(1)

# extracting text from page
#Extracting the content from page number 1
print(pageObj.extractText())
print("\n")

#Extracting the content from page number 2
print(pageObj1.extractText())
print("\n")

# closing the pdf file object
pdfFileObj.close()