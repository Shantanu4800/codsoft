# def sum(x, y):
#     return x + y

# def minus(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     if y != 0:
#         return x / y
#     else:
#         return "Cannot divide by zero"

# def main():
#     print("Simple Calculator")
#     print("Operations:")
#     print("1. sum")
#     print("2. minus")
#     print("3. Multiply")
#     print("4. Divide")

#     choice = input("Enter operation number (1/2/3/4): ")

#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))

#     if choice == "1":
#         print("Result:", sum(num1, num2))
#     elif choice == "2":
#         print("Result:", minus(num1, num2))
#     elif choice == "3":
#         print("Result:", multiply(num1, num2))
#     elif choice == "4":
#         print("Result:", divide(num1, num2))
#     else:
#         print("Invalid choice.")

# if __name__ == "__main__":
#     main()
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# import random

# def get_user_choice():
#     while True:
#         user_choice = input("Choose rock, paper, or scissors: ").lower()
#         if user_choice in ["rock", "paper", "scissors"]:
#             return user_choice
#         else:
#             print("Invalid choice. Please choose rock, paper, or scissors.")

# def get_computer_choice():
#     return random.choice(["rock", "paper", "scissors"])

# def determine_winner(user_choice, computer_choice):
#     if user_choice == computer_choice:
#         return "It's a tie!"
#     elif (
#         (user_choice == "rock" and computer_choice == "scissors") or
#         (user_choice == "scissors" and computer_choice == "paper") or
#         (user_choice == "paper" and computer_choice == "rock")
#     ):
#         return "You win!"
#     else:
#         return "Computer wins!"

# user_score = 0
# computer_score = 0

# while True:
#     user_choice = get_user_choice()
#     computer_choice = get_computer_choice()

#     print(f"You chose {user_choice}")
#     print(f"Computer chose {computer_choice}")

#     result = determine_winner(user_choice, computer_choice)
#     print(result)

#     if result == "osm You win!":
#         user_score += 1
#     elif result == "I win!":
#         computer_score += 1

#     print(f"Your score: {user_score}, Computer's score: {computer_score}")

#     play_again = input("Do you want to play again? (yes/no): ").lower()
#     if play_again != "yes":
#         break
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


import random

# Define the quiz questions and answers
quiz_questions = [
    {
        "question": "Epsom(England) is the place associated with?",
        "options": ["shooting", "Horse racing", "polo","snooker"],
        "correct_answer": "Horse racing",
    },
    {
        "question": "Golf Player Vijay Singh belongs to which country ?",
        "options": ["India", "Fiji", "UK","USA"],
        "correct_answer": "Fiji",
    },
    {
        "question": "in order to excele that we are entering a formula in a cell we must beging with?",
        "options": ["@", "$", "="],
        "correct_answer": "=",
    },
    {
        "question": "In how many generation a computer is classified'?",
        "options": ["3", "4", "5"],
        "correct_answer": "5",
    },
    {
        "question": "Which memory is volatile ?",
        "options": ["SRAM", "DRAM", "ROM"],
        "correct_answer": "ROM",
    },
    {
        "question": "The revolt of 1857 had its begining in ?",
        "correct_answer": "Meerut",
    },
]

def present_question(question_dict):
    print(question_dict["question"])
    if "options" in question_dict:
        for i, option in enumerate(question_dict["options"], start=1):
            print(f"{i}. {option}")
    user_answer = input("Your answer: ").strip()
    return user_answer

def evaluate_answer(question_dict, user_answer):
    correct_answer = question_dict["correct_answer"]
    if "options" in question_dict:
        correct_index = question_dict["options"].index(correct_answer) + 1
    else:
        correct_index = None

    if user_answer == correct_answer:
        return "Correct!"
    elif user_answer.isdigit() and int(user_answer) == correct_index:
        return "Correct!"
    else:
        return f"Incorrect. The correct answer is: {correct_answer}"

def main():
    random.shuffle(quiz_questions)
    user_score = 0

    print("Welcome to the Quiz Game!")
    print("You will be presented with a series of questions.")
    print("Please enter the number of your answer or type the answer for fill-in-the-blank questions.")

    for question in quiz_questions:
        user_answer = present_question(question)
        feedback = evaluate_answer(question, user_answer)
        print(feedback)

        if feedback == "Correct!":
            user_score += 1

    print(f"Quiz completed! Your score is: {user_score}/{len(quiz_questions)}")

if __name__ == "__main__":
    main()



































































