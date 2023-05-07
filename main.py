# Import the package we installed - are we supposed to re-install requests? pipenv install requests, was getting error but cleaned up files no errors
import requests
# Call .get() to a remote address - //
response = requests.get('https://httpbin.org/ip')
# Get our IP address from the response and print it in an f string
print('Your IP is {0}'.format(response.json()['origin']))

#Note that your database settings may differ
from peewee import *
import psycopg2 ; print(psycopg2)
#changed user to computer user from postgres and used commands to change password: whoami, \password treyweathers, then created postgres instead
db = PostgresqlDatabase('questions', user='postgres', password='hidden',
                        host='localhost', port=5432)
db.connect()
print('connected!')

import argparse #file system to pass in a file, do something to that file in your program, output the result
def file_parser(input_file, output_file=''):
    print(f'Processing {input_file}')
    print('Finished processing')
    if output_file:
        print(f'Creating {output_file}')
def main():
    parser = argparse.ArgumentParser('File parser')
    parser.add_argument('--infile', help='Input file')
    parser.add_argument('--out', help='Output file')
    args = parser.parse_args()
    if args.infile:
        file_parser(args.infile, args.out)
if __name__ == '__main__':
    main()

import random #choosing random choices
#import questions from sql database after debugging and fix functions

#function to grab a random question from a list of questions,
def cards ():
    #using global variables to access the questions outside the function
    global question
    global questions
    question = random.choice(questions)
    #then remove that question from the list so it doesn't get repeated
    questions.remove(question)
    print(question, '::::' , len(questions), '/')

#Shuffle the list of cards so that each time we run the program, we will have a different order of flash cards
#random.shuffle(questions)
print(cards)

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
    
#Once we've gon through all the flash cards  and restudied anything wrong, then print end of game message
print('All done!')