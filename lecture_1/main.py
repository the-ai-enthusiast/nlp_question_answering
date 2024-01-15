import read_resumes
from transformers import pipeline
import time

################################################################################################
################################  Get the contents of each resume as a string
################################################################################################
file_contents = read_resumes.file_contents


################################################################################################
################################  Go through each file and perform question answering
################################################################################################
qa_model = pipeline("question-answering", model="distilbert-base-cased-distilled-squad") # Model is 21 MB

for file_name, file_text in file_contents.items():
    start_time = time.time()
    question = "What kind of job is the person looking for?"
    # Perform question-answering
    answer = qa_model(question=question, context= file_text)
    end_time = time.time()

    # Print the answer
    print(f"------ Resume {file_name}: ------")
    print(f"Question: {question}")
    print(f"    Answer: {answer['answer']}")
    print(f"    Confidence: {answer['score']}")
    print(f"    Elapsed Time: {end_time - start_time} seconds\n")