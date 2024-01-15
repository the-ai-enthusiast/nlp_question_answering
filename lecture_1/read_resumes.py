

"""
This file will take in a folder and will loop through each of the resumes in the folder (only PDF format is supported for now)

For each one, it will extract the content of the file into a string :) 

"""

################################################################################################
################################ importing required modules
################################################################################################
import PyPDF2
import os

DEBUG = False

def print_debug(x):
    if DEBUG:
        print(x)


################################################################################################
################################  get all files in the folder path and store into dictionary of strings
################################################################################################
path_folder = '..\\sample_resumes'
print_debug(f"path_folder is {path_folder}")
# Use list comprehension to get all files in the folder
files = [f for f in os.listdir(path_folder) if os.path.isfile(os.path.join(path_folder, f)) and f.endswith('.pdf')]


file_contents = {} # dictionary where key is the filename and value is the text inside that PDF file (resume)

print_debug(files)
for file in files: 
    path = os.path.join(path_folder, file)

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
    file_contents[file] = string_contents
