import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"what is your name?",
        ["You can call me a chatbot", "My name is Bot", "I am a chatbot"]
    ],
    [
        r"how are you?",
        ["I'm doing good", "I am fine", "I am doing well, thank you"]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind"]
    ],
    [
        r"quit",
        ["Bye bye take care. It was nice talking to you :) "]
    ]
]

chatbot = Chat(pairs, reflections)
chatbot.converse()