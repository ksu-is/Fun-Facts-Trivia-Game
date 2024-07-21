import threading
import time
import random

# Define trivia questions and answers
questions=[
    {
        "question": "What is the capital city of Switzerland?",
        "options": {"A. Geneva", "B. Bern", "C. Zurich", "D. Lausanne"},
        "answer": "B"
    },
{
        "question": "What are animals that eat both plants and meat referred to as?",
        "options": ["A. Carnivores", "B. Herbivores", "C. Predators", "D. Omnivores"],
        "answer": "D"
    },
{
        "question": "What is the largest planet in the solar system",
        "options": ["A. Jupiter", "B. Saturn", "C. Earth", "D. Pluto"],
        "answer": "A"
    },
{
        "question": "What is the tallest mountain in the world?",
        "options": ["A. Himalayas", "B. Mt. Kilimanjaro", "C. Mt. Everest", "D. Denali"],
        "answer": "C"
    },
{
        "question": "How many teeth does an adult human have?",
        "options": ["A. 34", "B. 32", "C. 28", "D. 36"],
        "answer": "B"
    },
{
        "question": "What is the largest ocean in the world?",
        "options": ["A. Indian Ocean", "B. Atlantic Ocean", "C. Pacific Ocean", "D. Arctic Ocean"],
        "answer": "C"
    },
{
        "question": "How many countries are on the continent of Africa?",
        "options": ["A. 64", "B. 50", "C. 57", "D. 54"],
        "answer": "D"
    },
{
        "question": "What is the official language of Brazil?",
        "options": ["A. Portuguese", "B. Spanish", "C. Italian", "D. French"],
        "answer": "A"
    },
{
        "question": "How many starting players on one team can play on the field in a soccer match?",
        "options": ["A. 10", "B. 15", "C. 13", "D. 11"],
        "answer": "D"
    },
{
        "question": "Which country has the largest population in the world?",
        "options": ["A. United States of America", "B. India", "C. China", "D. Russia"],
        "answer": "C"
    },
]

score = 0
question_index = 0
game_over = False

def display_question():
    global question_index
    global game_over

    if question_index < len(questions):
        print("\nQuestion:")
        print(questions[question_index]["question"])

        timer_thread = threading.Timer(10, timer)
        timer_thread.start()

        user_answer = input("Your answer: ").strip().lower()

        timer_thread.cancel()

        correct_answer = questions[question_index]["answer"].lower()
        if user_answer == correct_answer:
            print("Correct!")
            global score
            score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")

        question_index += 1
    else:
        game_over = True

def timer():
    print("\nTime's up!")
    
    game_over = True

def main():
    global game_over
    print("Welcome to Jeton's Fun Facts Trivia Game!")
    print("You will have 10 seconds to answer each question.")
    input("Press Enter to Begin!")

    while not game_over:
        display_question()

    print("\nGame Over!")
    print(f"Your final score is: {score}/{len(questions)}")
    
if __name__ == "__main__":
    main()