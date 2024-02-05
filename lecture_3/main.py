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
model_name = 'yjernite/bart_eli5'
seq2seq_qa_model = pipeline('text2text-generation', model=model_name, tokenizer=model_name) # 1.63 GB model

def get_answer(question, context):
    answer = seq2seq_qa_model(
        f"question: {question} context: {context}",
        num_beams=4,
        do_sample=True,
        temperature=.5,
        max_length=64
    )
    return answer

################################################################################################
################################ 4. Go through each file and perform question answering
################################################################################################ pip freeze > requirements. txt
for file_name, file_text in file_contents.items():
    start_time = time.time()
    # question = "What kind of job is the person looking for?"
    # question = "In the context section, there is a resume of a random person. Looking at the resume - what kind of job is most suitable for the description provided?" 
    # question = " You are a recruiter. In the context section, there is a resume of a random person. Looking at the person's resume - what kind of job is the person most suitable for?"  
    question = "You are a recruiter. In the context section, there is a resume belonging to John. What kind of job is John most suitable for?"                  ########################## worked the best
    # Perform question-answering
    answer = get_answer(question=question, context= file_text)
    end_time = time.time()

    # Print the answer
    print(f"------ Resume {file_name}: ------")
    print(f"Question: {question}")
    print(f"    Answer: {answer[0]['generated_text']}")
    print(f"    Elapsed Time: {end_time - start_time} seconds\n")