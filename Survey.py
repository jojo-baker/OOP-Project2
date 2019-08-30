from Section import Section
from Question import Question
from Answer import Answer

class Survey:

    def __init__(self):
        pass

    def start_survey(self):
        pass

# Welcome message
print('\nWelcome to my survey!\nPlease answer honestly.')

# Here are the first three qualifying questions
question_prompts = [
    '\n----------Q1----------\nSomething about Wednesday\'s class\n(a) Yes\n(b) No\n\n',
    '\n----------Q2----------\nSomething about Saturday\'s class\n(a) Yes\n(b) No\n\n',
    '\n----------Q3----------\nSomething about the mentors \n(a) Yes\n(b) No\n\n',
]
qualifying_questions = [
    Question(question_prompts[0], ' '),
    Question(question_prompts[1], ' '),
    Question(question_prompts[2], ' '),
]

# Here is the first section - title, description and questions
# Section 1 title and descripion
section1 = Section('\n\n*****************************\n       Section 1 Title\n*****************************', '\nSection 1 Description')
# Section 1 questions
section1_question_prompts = [
   '\n----------SQ1----------\nFirst section question\n(a) answer 1\n(b) answer 2\n(c) answer 3\n\n',
   '\n----------SQ2----------\nFirst section question\n(a) answer 1\n(b) answer 2\n(c) answer 3\n\n',
   '\n----------SQ3----------\nFirst section question\n(a) answer 1\n(b) answer 2\n(c) answer 3\n\n',
]
section1_questions = [
    Question(section1_question_prompts[0], ' '),
    Question(section1_question_prompts[1], ' '),
    Question(section1_question_prompts[2], ' '),
]



# Here is the second section - title, description and questions
# Section 2 title and descripion
section2 = Section('\n\n*****************************\n       Section 2 Title\n*****************************', '\nSection 2 Description')
# Section 2 questions
section2_question_prompts = [
   '\n----------SQ1----------\nSecond section question\n(a) answer 1\n(b) answer 2\n(c) answer 3\n\n',
   '\n----------SQ2----------\nSecond section question\n(a) answer 1\n(b) answer 2\n(c) answer 3\n\n',
   '\n----------SQ3----------\nSecond section question\n(a) answer 1\n(b) answer 2\n(c) answer 3\n\n',
]
section2_questions = [
    Question(section2_question_prompts[0], ' '),
    Question(section2_question_prompts[1], ' '),
    Question(section2_question_prompts[2], ' '),
]

# Here is the third section - title, description and questions
# Section 3 title and descripion
section3 = Section('\n\n*****************************\n       Section 3 Title\n*****************************', '\nSection 3 Description')
# Section 3 questions
section3_question_prompts = [
   '\n----------SQ1----------\nThird section question\n(a) answer 1\n(b) answer 2\n(c) answer 3\n\n',
   '\n----------SQ2----------\nThird section question\n(a) answer 1\n(b) answer 2\n(c) answer 3\n\n',
   '\n----------SQ3----------\nThird section question\n(a) answer 1\n(b) answer 2\n(c) answer 3\n\n',
]
section3_questions = [
    Question(section3_question_prompts[0], ' '),
    Question(section3_question_prompts[1], ' '),
    Question(section3_question_prompts[2], ' '),
]

# Section 1 Function
def run_section1(section1_questions):
    print(section1.section_title)
    print(section1.description)
    for question in section1_questions:
        while True:
            answer = input(question.prompt)
            if answer.lower() in ['a', 'b', 'c']:
                print('***** Great, you answered ' + answer)
                break
            else:
                print('***** Nope, not valid. Try that again. I\'m only accepting a, b or c.')
# Section 2 Function
def run_section2(section2_questions):
    print(section2.section_title)
    print(section2.description)
    for question in section2_questions:
        while True:
            answer = input(question.prompt)
            if answer.lower() in ['a', 'b', 'c']:
                print('***** Great, you answered ' + answer)
                break
            else:
                print('***** Nope, not valid. Try that again. I\'m only accepting a, b or c.')
# Section 3 Function
def run_section3(section3_questions):
    print(section3.section_title)
    print(section3.description)
    for question in section3_questions:
        while True:
            answer = input(question.prompt)
            if answer.lower() in ['a', 'b', 'c']:
                print('***** Great, you answered ' + answer)
                break
            else:
                print('***** Nope, not valid. Try that again. I\'m only accepting a, b or c.')


#this is the start of the survey qualifying questions, but it isn't executed until the bottom
def run_survey(qualifying_questions):
    sections_to_show = []
    for question in qualifying_questions:
        while True:
            answer = input(question.prompt)
            if answer.lower() in ['a', 'b', 'yes', 'no']:
                # if the answer is valid then process it
                print('***** Awesome, you answered ' + answer)
                if answer.lower() in ['a', 'yes']:
                    # if the answer is yes, then save this section for later
                    sections_to_show.append('a')
                else:
                    sections_to_show.append('b')
                break
            else:
                print('***** Hmmmmmmm, that\'s not quite right...Please try again.')
    if sections_to_show[0] == 'a':
        run_section1(section1_questions)
    if sections_to_show[1] == 'a':
        run_section2(section2_questions)
    if sections_to_show[2] == 'a':
        run_section3(section3_questions)

# This starts the survey
run_survey(qualifying_questions)

# This is the end message
print('\nThanks so much for taking the survey. Have a great day!\n\n')