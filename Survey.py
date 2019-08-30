from Section import Section
from Question import Question

class Survey:

    def __init__(self):
        pass

    def start_survey(self):
        pass

# Welcome message
print('\nWelcome to the SheCodes survey!\nPlease answer honestly.')

# Here are the first three qualifying questions
question_prompts = [
    '\n---------- Question 1 ----------\nDid you attend Wednesday\'s class?\n(a) I wouldn\'t miss it!\n(b) Unfortunately I couldn\'t make it.\n\n',
    '\n---------- Question 2 ----------\nDid you attend Saturday\'s class?\n(a) Absolutely!\n(b) Not this time.\n\n',
    '\n---------- Question 3 ----------\nDo you feel you\'re learning a lot from the mentors?\n(a) A thousand times YES!\n(b) Not really, no.\n\n',
]
qualifying_questions = [
    Question(question_prompts[0], ' '),
    Question(question_prompts[1], ' '),
    Question(question_prompts[2], ' '),
]

# Here is the first section - title, description and questions
# Section 1 title and descripion
section1 = Section('\n\n*****************************\n     About Wednesday...\n*****************************', '\nThis round of questions is all about the Wednesday session you attended.')
# Section 1 questions
section1_question_prompts = [
   '\n---------- Wednesday Question 1 ----------\nHow did you find the content?\n(a) Easy to follow.\n(b) A little hard to follow.\n(c) I was completely lost...\n\n',
   '\n---------- Wednesday Question 2 ----------\nWere you able to complete the night\'s task?\n(a) Yes I finished it in class.\n(b) I couldn\'t finish it in class, but I finished it at home.\n(c) No, it\'s another thing I\'m behind on :(\n\n',
   '\n---------- Wednesday Question 3 ----------\nDid you enjoy the session?\n(a) I loved it!\n(b) It was fine, but I\'ve had better.\n(c) I literally wanted to cry (or did cry).\n\n',
]
section1_questions = [
    Question(section1_question_prompts[0], ' '),
    Question(section1_question_prompts[1], ' '),
    Question(section1_question_prompts[2], ' '),
]



# Here is the second section - title, description and questions
# Section 2 title and descripion
section2 = Section('\n\n*****************************\n      About Saturday...\n*****************************', '\nThis round of questions is all about the Saturday class you attended.')
# Section 2 questions
section2_question_prompts = [
   '\n---------- Saturday Question 1 ----------\nHow did you find the demo?\n(a) Very valuable!\n(b) It was fine, but I was a little lost.\n(c) Confusing!\n\n',
   '\n---------- Saturday Question 2 ----------\nDid you finish all the tasks in class?\n(a) Yes, I got them all done.\n(b) Most, but not all of them.\n(c) I finished very little...\n\n',
   '\n---------- Saturday Question 3 ----------\nDid you make any progress on this week\'s project?\n(a) Yep, I sure did!\n(b) Not much no.\n(c) I didn\'t make any progress.\n\n',
]
section2_questions = [
    Question(section2_question_prompts[0], ' '),
    Question(section2_question_prompts[1], ' '),
    Question(section2_question_prompts[2], ' '),
]

# Here is the third section - title, description and questions
# Section 3 title and descripion
section3 = Section('\n\n*****************************\n    About those mentors...\n*****************************', '\nWe\'d like to hear your thoughts on the mentors.')
# Section 3 questions
section3_question_prompts = [
   '\n---------- Mentors Question 1 ----------\nWere they on their game this week?\n(a) Couldn\'t rate them any higher.\n(b) They\'ve had better weeks.\n(c) Lol, they don\'t have game.\n\n',
   '\n---------- Mentors Question 2 ----------\nWho was your favourite mentor from this week?\n(a) Hayley\n(b) Marc\n(c) Ben\n\n',
   '\n---------- Mentors Question 3 ----------\nAre you getting enough help from the mentors on Slack?\n(a) Yes, heaps.\n(b) I ask questions, but they sometimes don\'t answer them.\n(c) I don\'t really ask any questions...\n\n',
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