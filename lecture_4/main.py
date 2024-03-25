

"""

Step 1. Extract the text from the PDF file - get each page of Lord of the Rings
Step 2. Split the text  into pages and then make an embedding of each page USING an embedding model 
Step 3. Store embeddings into the Vector Database
Step 4. Have a Question you Ask
Step 5. Embed the question - find the most similar document/page from the Novel 
Step 6. Use a closed QA (lecture 2) or open abstractive (lecture 3) QA model to answer the question :) 

"""

from novel_pages import novel_dictionary
from transformers import pipeline
import time
import novel_pages
import chromadb
import os

########################################################################
# Step 1. Extract the text from the PDF file - get each page of Lord of the Rings
########################################################################
novel_dictionary = novel_pages.novel_dictionary # {page_num : text_string} -this is a dictionary with page number as key and text as value


########################################################################
# Step 2 + 3. Split the text into pages and then make an embedding of each page USING an embedding model. Store this in the vector database
########################################################################

### create location of vector database (we will use filebased DB)
db_folder_path = './vector_db/'

# Create folder if it doesn't exist
if not os.path.exists(db_folder_path):
    os.makedirs(db_folder_path)

client = chromadb.PersistentClient(path=db_folder_path)


collection_name = 'lord_of_the_rings'

# https://docs.trychroma.com/api-reference
## get list of collections in Database
name_of_collections = set([x.name for x in  client.list_collections()])

## if it's not there we will create the collection and put in the documents
if collection_name not in name_of_collections:
    client.create_collection(name=collection_name)

## get the collection
collection = client.get_or_create_collection(name = collection_name)

## store text into the database - behind the scenes it will automtically create embeddings from the text
collection.add(
    documents = [x for x in list(novel_dictionary.values())],
    metadatas = [{"source": "book"} for x in novel_dictionary],
    ids = [str(x) for x in novel_dictionary]
)

########################################################################
# Step 4. + 5. Have a Question you Ask - find the most similar document/page from the Novel -> Chroma handles this for us -> 
### using the embedding function that we already have
########################################################################
question = "What is Strider's real name?"

results = collection.query(
    query_texts=[question],
    n_results=2
)

document_found = results['documents'][0][1]
 
print(f"=========> Most similar page to the question: {document_found[:100]} \n\n")

########################################################################
# Step 6. Use a closed QA (lecture 2) or open abstractive (lecture 3) QA model to answer the question :) 
## As an example: We will use the closed QA model from lecture 2 to answer the question
########################################################################

qa_model = pipeline("question-answering", model="distilbert-base-cased-distilled-squad") # Model is 21 MB

def get_answer(question, context):
    answer = qa_model(question=question, context=context)
    return answer



start_time = time.time()
# Perform question-answering
answer = get_answer(question=question, context= document_found)
end_time = time.time()

# Print the answer
print(f"Question: {question}")
print(f"    Answer: {answer['answer']}")
print(f"    Confidence: {answer['score']}")
print(f"    Elapsed Time: {end_time - start_time} seconds\n")