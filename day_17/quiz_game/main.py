from random import shuffle
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


def main():
    question_bank = [Question(data) for data in question_data]
    shuffle(question_bank)
    quiz_brain = QuizBrain(question_bank)

    score = 0
    while quiz_brain.has_question():
        result = quiz_brain.next_question()

        if result:
            score += 1
            print("Correct!")
        else:
            print("Wrong!")

        print("Score: " + str(score))

    print("End of the Quiz Brain!")
    print(f"Score: {score} out of {len(question_bank)} or {round(100 * score / len(question_bank), 2)}% correct answers")


if __name__ == "__main__":
    main()
