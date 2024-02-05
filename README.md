



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
    1. if you don't have a virtual environment created from Lecture 2 above - follow steps 1-7 (including step 7) from Lecture 2. Otherwise, you already have virtual environment, just activate it - cd to "myenv" folder. Then activate it by ".\Scripts\activate"
    2. now you must go into lecture 2 by "cd lecture_3"
    3. [Learn the concept] you can open up the interactive.ipynb to play around with the QA software interactively
    4. [Run the code] - run the main.py script "python main.py"

