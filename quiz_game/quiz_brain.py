class QuizBrain:
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text}. (True/False)?:")
        self.check_answer(user_answer,question.answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("That's Correct")
            self.score += 1
        else:
            print(f"Wrong. the answer is {correct_answer}")

        print(f"Your current score is : {self.score}/{self.question_number}")
        print("\n")



