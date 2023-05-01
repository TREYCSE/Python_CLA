import random #choosing random choices
import os #operating system - for finding files on the computer

#python3 app.py

#function to grab a random question from a list of questions,
def cards ():
    #using global variables to access the questions outside the function
    global question
    global questions
    question = random.choice(questions)
    #then remove that question from the list so it doesn't get repeated
    questions.remove(question)
    print(question, '::::' , len(questions), '/')

#Access a folder on the computer using the folder's path to search for files
path = 'C:/Users/treyweathers/Desktop/THE_PLAN/1_EDUCATION/APP_DEV/GENASSEM_FULLSTACK/CODES/Python_CLA/files'
files = os.listdir(path)
#A list of names eof these file paths are stored as a list in the variable files

#The only files we want are text files so we are removing files that are not txt
for file in files:
    if 'txt' not in file:
        files.remove(file)

#Shuffle the list of files so that each time we run the program, we will have a different order of flash cards
random.shuffle(files)

#Creating a full path for each file
for file in files:
    print('#', file, '#')
    file = path + '/' + file

#opening the file and reading its contents
    with open(file) as f: 
        lines = f.readlines()

#CONDITIONALS - y or n

