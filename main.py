from question_model import Question
from data import questions
from quiz_game import QuizGame

question_bank = []

for question in questions:
    question_bank.append(Question(question["text"], question["answer"]))

game = QuizGame(question_bank)

for i in range(0, len(question_bank)):
    question_text = game.ask_question()
    answer = input(question_text)
    result= game.check_answer(answer)

    if result:
        print("Answer is correct")
    else:
        print("Answer is incorrect")
    print(game.get_score_report())