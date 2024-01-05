class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.questions_list = question_list
        self.score = 0

    def check_answer(self, answer,correct_answer):
        if answer.lower() == correct_answer.lower():
            print("you got it right!")
            self.score += 1
            print(f"Your current score is {self.score}/{self.question_number}")
        else:
            print("That's wrong.")

        print(f"the correct answer is: {correct_answer}")
        print("\n")

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        q = self.questions_list[self.question_number].text
        a = self.questions_list[self.question_number].answer

        self.question_number += 1
        ans = input(f"Q.{self.question_number}: {q} (True/False)?:")
        self.check_answer(ans,a)
