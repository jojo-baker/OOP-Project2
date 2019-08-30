from Section import Section
from Question import Question
from Answer import Answer

class Survey:

    def __init__(self):
        pass

    def start_survey(self):
        pass

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


# section1_question_prompts = [
#    '\n----------SQ1----------\nFirst section question\n(a) answer 1\n(b) answer 2\n(c) answer 3\n\n',
#    '\n----------SQ1----------\nFirst section question\n(a) answer 1\n(b) answer 2\n(c) answer 3\n\n',
#    '\n----------SQ1----------\nFirst section question\n(a) answer 1\n(b) answer 2\n(c) answer 3\n\n',
# ]
# section1_questions = [
#     Question(section1_question_prompts[0], ' '),
#     Question(section1_question_prompts[2], ' '),
#     Question(section1_question_prompts[3], ' '),
# ]


print('Welcome to my survey!\nPlease answer honestly.')


def run_survey(qualifying_questions):
    """ process the survey """
    sections_to_show = []
    for question in qualifying_questions:
        while True:
            answer = input(question.prompt)
            if answer.lower() in ['a', 'b', 'yes', 'no']:
                # if the answer is valid then process it
                print('=======================\nAwesome, you answered ' + answer + '\n=======================')
                if answer.lower() in ['a', 'yes']:
                    # if the answer is yes, then save this section for later
                    sections_to_show.append('a')
                else:
                    sections_to_show.append('b')
                break
            else:
                print('===========================================================\nHmmmmmmm, that\'s not quite right...Please try again\n===========================================================')
    if sections_to_show[0] == 'a':
        print('this is the first section')

    if sections_to_show[1] == 'a':
        print('this is the second section')
    if sections_to_show[2] == 'a':
        print('this is the third section')

# This starts the survey
run_survey(qualifying_questions)

