"""
CodeAlpha - Task 4: Basic Chatbot
A simple rule-based chatbot using if-elif matching.
"""

import random

RESPONSES = {
    "hello": ["Hi!", "Hello there!", "Hey! How can I help?"],
    "hi": ["Hi!", "Hello!"],
    "how are you": [
        "I'm fine, thanks! How about you?",
        "Doing great, thanks for asking!"
    ],
    "what is your name": [
        "I'm a simple chatbot built for the CodeAlpha internship."
    ],
    "what can you do": [
        "I can chat with you about basic things. "
        "Try saying hello, or ask how I am!"
    ],
    "thank you": ["You're welcome!", "Anytime!"],
    "thanks": ["No problem!", "You're welcome!"],
    "bye": ["Goodbye!", "See you later!", "Bye! Take care."],
}

EXIT_WORDS = {"bye", "exit", "quit"}


def get_response(user_input):
    text = user_input.lower().strip()

    for key, replies in RESPONSES.items():
        if key in text:
            return random.choice(replies)

    return "Sorry, I didn't understand that. Could you rephrase?"


def chat():
    print("Chatbot: Hi! Type 'bye' to end the conversation.\n")

    while True:
        user_input = input("You: ")
        text = user_input.lower().strip()

        response = get_response(user_input)
        print("Chatbot:", response)

        if text in EXIT_WORDS or "bye" in text:
            break


if __name__ == "__main__":
    chat()
