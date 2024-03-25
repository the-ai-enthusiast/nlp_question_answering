
import os
import requests
import PyPDF2


def extract_pages(input_pdf_path, start_page, end_page=-1):
    result_dict = {}
    try:
        with open(input_pdf_path, 'rb') as input_file:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfReader(input_file)

            num_pages = len(pdf_reader.pages)
            if end_page == -1:
                end_page = num_pages
            # Validate start_page and end_page
            if not (1 <= start_page <= end_page <= len(pdf_reader.pages)):
                raise ValueError("Invalid page range")

            # Extract pages from start_page to end_page
            for page_num in range(start_page - 1, end_page):
                page_text = pdf_reader.pages[page_num].extract_text()
                result_dict[page_num+1] = page_text
    except Exception as e:
        print(f"Error: {e}")
    return result_dict

# Define the URL and folder path
### Lord of the Rings : Available on Online Archive: https://archive.org/details/j-r-r-tolkien-lord-of-the-rings-01-the-fellowship-of-the-ring-retail-pdf/page/n5/mode/2up
pdf_url = 'https://ia601003.us.archive.org/3/items/j-r-r-tolkien-lord-of-the-rings-01-the-fellowship-of-the-ring-retail-pdf/j-r-r-tolkien-lord-of-the-rings-01-the-fellowship-of-the-ring-retail-pdf.pdf'
save_folder = './downloaded_novel/'
pdf_filename = os.path.join(save_folder, 'lord_of_the_rings.pdf')

novel_dictionary = {}

# Create folder if it doesn't exist
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

if not os.path.exists(pdf_filename):
    # Send GET request to download PDF content
    response = requests.get(pdf_url)

    # Check if request was successful and save PDF to file
    if response.status_code == 200:
        with open(pdf_filename, 'wb') as f:
            f.write(response.content)
        print("PDF downloaded successfully")
    else:
        print("Failed to download PDF")
        1/0 ### throw an exception

# read in the PDF from filepath
novel_dictionary = extract_pages(pdf_filename, 1, -1)



