# Basic Chatbot - CodeAlpha Internship Task

A simple rule-based chatbot that replies to the user with predefined responses.

## Features
- Understands greetings, "how are you", name questions, thanks and goodbyes
- Case-insensitive and ignores punctuation ("Hello!" works the same as "hello")
- Handles empty input and unknown messages gracefully
- Keeps chatting in a loop until the user says bye

## Concepts Used
if-elif | functions | loops | input/output

## Project Structure
```
CodeAlpha_BasicChatbot/
|-- chatbot.py     # Python version
|-- Chatbot.java   # Java version
|-- README.md
`-- .gitignore
```

## How to Run

**Python** (3.6+)
```bash
python chatbot.py
```

**Java** (JDK 8+)
```bash
javac Chatbot.java
java Chatbot
```

## Sample Conversation
```
You: hello
Bot: Hi!
You: how are you
Bot: I'm fine, thanks!
You: what is the weather
Bot: Sorry, I don't understand that. Type 'help' to see what I can say.
You: bye
Bot: Goodbye!
```

## Author
**Anirudh** - CodeAlpha Intern
