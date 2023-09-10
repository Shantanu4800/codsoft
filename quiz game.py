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
