from text_extractor import Text_Extractor
from transformers import pipeline
import time
import os
from print_utils import print_debug

################################################################################################
################################ 1. get all files in the folder path and store into dictionary of strings
################################################################################################
path_folder = '..\\sample_resumes'
print_debug(f"path_folder is {path_folder}")
# Use list comprehension to get all files in the folder
files = [f for f in os.listdir(path_folder) if os.path.isfile(os.path.join(path_folder, f)) and f.endswith('.pdf')]



################################################################################################
################################ 2. Extract the text from each file and store into dictionary of strings
################################################################################################
text_extractor = Text_Extractor() # initialize the text extractor

file_contents = {} # dictionary where key is the filename and value is the text inside that PDF file (resume)

for file in files: 
    path = os.path.join(path_folder, file) ### make the path to the file by joining the folder path and the file name
    print_debug(f"path is {path}")
    string_contents = text_extractor.extract_text(path) ### extract the text from the file and store it in the dictionary
    file_contents[file] = string_contents

################################################################################################
################################ 3. Initialize the model 
################################################################################################
qa_model = pipeline("question-answering", model="distilbert-base-cased-distilled-squad") # Model is 21 MB

def get_answer(question, context):
    answer = qa_model(question=question, context=context)
    return answer

################################################################################################
################################ 4. Go through each file and perform question answering
################################################################################################
for file_name, file_text in file_contents.items():
    start_time = time.time()
    question = "What kind of job is the person looking for?"
    # Perform question-answering
    answer = get_answer(question=question, context= file_text)
    end_time = time.time()

    # Print the answer
    print(f"------ Resume {file_name}: ------")
    print(f"Question: {question}")
    print(f"    Answer: {answer['answer']}")
    print(f"    Confidence: {answer['score']}")
    print(f"    Elapsed Time: {end_time - start_time} seconds\n")