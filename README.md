



## To get started:
### Lecture 1:
 - Introductory Video - no code :) 
 - link to the video is here: https://youtu.be/gvd1YUKPGXU?si=np5cZqb2jaHz4klT  
### Lecture 2: Extractive QA 
 - #### Description: Answer is literally in the background text we provide
 - #### Follow Steps: 
    1. cd to the root directory of git repository
    2. then go up one directory by doing "cd .."
    3. then "python -m venv myenv"
    4. if you run into permission issues on Windows 11: https://stackoverflow.com/questions/4037939/powershell-says-execution-of-scripts-is-disabled-on-this-system
    5. now you have a virtual environment, you can then activate it ".\myenv\Scripts\activate"
    6. now you are inside of the virtual environment , "cd question_answering_tutorials"
    7. now you are in the root directory of the git repository, type in "pip install -r .\requirements.txt" to install all the dependencies of the project
    8. now you must go into lecture 2 by "cd lecture_2"
    9. then run the main.py script "python main.py"
### Lecture 3: Open Generative QA 
 - #### Description: Answer is from the text but can/will have additional supporting text generated from the model
 - #### Follow Steps: 
    1. if you don't have a virtual environment created from Lecture 2 above - follow steps 1-7 (including step 7) from Lecture 2. Otherwise, you already have virtual environment, just activate it - cd to "myenv" folder. Then activate it by ".\Scripts\activate". Then run step 7 above.
    2. now you must go into lecture 3 by "cd lecture_3"
    3. [Learn the concept] you can open up the interactive.ipynb to play around with the QA software interactively
      - also watch the Youtube Video Lecture 3a and 3b - playlist: https://www.youtube.com/watch?v=gvd1YUKPGXU&list=PLY9-HZ9p-BOb4qi-FLphlBsbD6BnRVUuT
    4. [Run the code] - run the main.py script "python main.py"
### Lecture 4: Break up text by Using Embedding Model with a Vector Database
 - #### Description: What Happens When We Have to do QA on Very Large Text Documents or on multiple documents? Many models have a set context length of how many word tokens they can except. Therefore, for large texts, to do QA, we will break up the large text file into chunks. For each chunk: we use an Embedding Model to encode the chunk of text into a single vector that represents the concepts inside the chunk of text. We can store this vector into a Vector Database.

 Then when we get a question - we can encode the question using the embedding model -> we can compare the question's vector to each vector in the Vector Database and find the chunk of text that is most similar. With the corresponding chunk of text that whose vector is the closest to the question's vector, we will now feed in this text into the QA Model. So now, we have 1 Embedding Model and 1 QA model (extractive QA vs open generative QA in Lecture 2 and Lecture 3)
 - #### Follow Steps: 
    1. if you don't have a virtual environment created from Lecture 2 above - follow steps 1-7 (including step 7) from Lecture 2. Otherwise, you already have virtual environment, just activate it - cd to "myenv" folder. Then activate it by ".\Scripts\activate". Then run step 7 from Lecture 2 to install all the dependency python files. 
    2. now you must go into lecture 4 by "cd lecture_4"
    3. [Learn the concept]  - Watch the Youtube Video Lecture 4 (not lecture 3b!) - playlist: https://www.youtube.com/watch?v=gvd1YUKPGXU&list=PLY9-HZ9p-BOb4qi-FLphlBsbD6BnRVUuT
    4. [Run the code] - run the main.py script "python main.py"


