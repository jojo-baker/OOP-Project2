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

questions = [
    Question(question_prompts[0], ' '),
    Question(question_prompts[1], ' '),
    Question(question_prompts[2], ' '),
]

print('Welcome to my survey!\nPlease answer honestly.')


def run_survey(questions):
    for question in questions:
        answer = input(question.prompt)
        # if answer == 'a' or answer == 'b' or answer == 'c':
        #     print('You answered ' + answer)
        # else:
        #     print('Hmmmmmmm...Please answer either a, b, or c')
        # trying the while loop



run_survey(questions)

# print('Welcome to this super special survey!\nPlease take the time to answer honestly.')
# print()
# print('------------ Question 1 ------------')
# print(q_text[0])
# answer1 = input()

# ask 3 qualifying questions with multiple choice answers
# section 1
# question with multiple choice answers