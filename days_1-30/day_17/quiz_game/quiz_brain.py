from question_model import Question


class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank

    def check_answer(self, answer):
        bool_answer = answer == "t" or answer == ""
        return bool_answer == self.question_list[self.question_number - 1].answer

    def has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1

        answer = input(f"Q.{self.question_number}: {question.text} [T/f]: ").lower()
        return self.check_answer(answer)
