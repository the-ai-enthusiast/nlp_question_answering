import PyPDF2
from print_utils import print_debug

class Text_Extractor:
    def __init__(self) -> None:
        pass 
    def extract_text(self, path):
        # creating a pdf file object
        pdfFileObj = open(path, 'rb')
        # creating a pdf reader object
        pdfReader = PyPDF2.PdfReader(pdfFileObj)

        # print_debuging number of pages in pdf file
        # print_debug(len(pdfReader.pages))

        # creating a page object
        pageObj = pdfReader.pages[0]

        # extracting text from page
        string_contents = pageObj.extract_text()

        # closing the pdf file object
        pdfFileObj.close()
        return string_contents