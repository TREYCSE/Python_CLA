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
for line in lines:
    line = line.split(',')
    for l in line:
        question.append(1)
    while '' in questions:
        questions.remove('')
    total_questions = len(questions)
        

#going through list of questions and inputing a y for yes and n for no.
unknown = []
for i in range (total_questions):
    cards()
    answer = input('y or n:',)
    #if we don't know the correct answer/unknown, put an n in, and place it into the unknown list
    if answer == 'n':
        unknown.append(question)

#^^Which will go back to be randomized again so we can keep moving through the unknown list until finished
while len(unknown) > 0:
    total_questions = len(unknown)
    questions = unknown
    unknown = []
    for i in range (total_questions):
        cards()
        answer = input('y or n:',)
        if answer == 'n':
            unknown.append(question)
        print(unknown)
    
#Once we've gon through all the flash cards/files of the folder and restudied anything wrong, then print end of game message
print('All done!')


#argparse or click requirements?, and what doing with peewee and pipenv?
#What is the format in txt file to be read for questions? - where is this data coming from?
#FileNotFoundError: [Errno 2] No such file or directory: '/files'

    
    


