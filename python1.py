class QuizGame:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question, options, correct_option):
        self.questions.append({
            'question': question,
            'options': options,
            'correct_option': correct_option
        })

    def display_question(self, question_dict):
        print(question_dict['question'])
        for idx, option in enumerate(question_dict['options']):
            print(f"{idx + 1}. {option}")

    def display_final_score(self):
        print(f"Your final score: {self.score}/{len(self.questions)}")

    def start_game(self):
        for question in self.questions:
            self.display_question(question)
            user_answer = input("Enter your choice (1-4): ")
            if user_answer.isdigit():
                user_answer = int(user_answer)
                if 1 <= user_answer <= len(question['options']):
                    if question['options'][user_answer - 1] == question['correct_option']:
                        print("Correct!")
                        self.score += 1
                    else:
                        print("Incorrect. The correct answer is:", question['correct_option'])
                else:
                    print("Invalid input. Please enter a number between 1 and", len(question['options']))
            else:
                print("Invalid input. Please enter a number.")
            print()  # Adding a newline for better readability

# Creating an instance of the quiz game
quiz = QuizGame()

# Adding questions to the quiz
quiz.add_question("What is the capital of France?",
                  ["Paris", "Rome", "London", "Berlin"],
                  "Paris")
quiz.add_question("Which planet is known as the Red Planet?",
                  ["Mars", "Venus", "Earth", "Jupiter"],
                  "Mars")
quiz.add_question("What is the chemical symbol for water?",
                  ["H2O", "CO2", "O2", "H2SO4"],
                  "H2O")

# Starting the quiz
quiz.start_game()

# Displaying the final score
quiz.display_final_score()
