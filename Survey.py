from Section import Section
from Question import Question
from Answer import Answer

class Survey:

    def __init__(self):
        pass

    def start_survey(self):
        pass

question_prompts = [
    '\n----------Q1----------\nThis is question number 1\n(a) answer 1\n(b) answer 2\n(c) answer 3\n\n',
    '\n----------Q2----------\nThis is question number 2\n(a) answer 1\n(b) answer 2\n(c) answer 3\n\n',
    '\n----------Q3----------\nThis is question number 3\n(a) answer 1\n(b) answer 2\n(c) answer 3\n\n',
]

qualifying_questions = [
    Question(question_prompts[0], ' '),
    Question(question_prompts[1], ' '),
    Question(question_prompts[2], ' '),
]

print('Welcome to my survey!\nPlease answer honestly.')


def run_survey(qualifying_questions):
    for question in qualifying_questions:
        while True:
            answer = input(question.prompt)
            if answer in ['a', 'b', 'c']:
                print('===== Awesome, you answered ' + answer + ' =====')
                break
            else:
                print('===== Hmmmmmmm, that\'s not quite right...Please answer either a, b, or c =====')


run_survey(qualifying_questions)



# ask 3 qualifying questions with multiple choice answers
# section 1
# question with multiple choice answers