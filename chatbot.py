import nltk
from nltk.chat.util import Chat, reflections

# Required for processing
# nltk.download('punkt') 

# Define pairs: (pattern, response)
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!", "Hi! How can I help?"]
    ],
    [
        r"what is your name ?",
        ["I am a helpful AI Chatbot created with NLTK.",]
    ],
    [
        r"how are you ?",
        ["I'm doing great! How are you?",]
    ],
    [
        r"sorry (.*)",
        ["No problem at all.", "Don't worry about it.",]
    ],
    [
        r"quit",
        ["Bye! Have a great day!", "Goodbye!"]
    ],
    [
        r"(.*)",
        ["That's interesting! Tell me more.", "I'm not sure I understand, can you rephrase?"]
    ]
]

def start_chatbot():
    print("Hi! I'm your NLP Chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    start_chatbot()
