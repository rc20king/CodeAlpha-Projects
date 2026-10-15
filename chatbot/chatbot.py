"""
CodeAlpha Internship - Task: Basic Chatbot
A simple rule-based chatbot using predefined replies.
Concepts used: if-elif, functions, loops, input/output.
"""

import string


def clean_input(text):
    """Lowercase the text and remove punctuation so matching is easier."""
    text = text.lower().strip()
    return text.translate(str.maketrans("", "", string.punctuation))


def get_response(user_input):
    """Return a predefined reply based on what the user typed."""
    message = clean_input(user_input)

    if message in ("hello", "hi", "hey"):
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message in ("what is your name", "whats your name", "who are you"):
        return "I'm CodeBot, a simple rule-based chatbot."
    elif message in ("help", "what can you do"):
        return "Try saying: hello, how are you, what is your name, thanks, or bye."
    elif message in ("thanks", "thank you"):
        return "You're welcome!"
    elif message in ("bye", "goodbye", "exit", "quit"):
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that. Type 'help' to see what I can say."


def main():
    print("=== BASIC CHATBOT ===")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")
        if not user_input.strip():
            print("Bot: Please type something.")
            continue

        reply = get_response(user_input)
        print("Bot:", reply)

        if reply == "Goodbye!":
            break


if __name__ == "__main__":
    main()
