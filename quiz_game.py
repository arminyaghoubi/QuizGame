from question_model import Question


class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.number_of_question = 0
        self.current_question: Question
        self.score = 0

    def ask_question(self):
        self.current_question = self.questions[self.number_of_question]
        self.number_of_question += 1
        return f"{self.number_of_question + 1} - {self.current_question.text} (True/False): "

    def check_answer(self, answer):
        if self.current_question.answer == answer:
            self.score += 1
            return True
        return False

    def get_score_report(self):
        return f"Your current score is: {self.score}/{self.number_of_question}"
