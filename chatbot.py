import nltk
from nltk.chat.util import Chat, reflections

pairs = [   
   [
    r"my name is (,*)",  
    ["Hello, %1, how can I help you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there", ]
    ]
]
chatbot = Chat(pairs, reflections)

def chat(): 
    print("Hello, I am your chatbot. How can I assist you today?")
    while True: 
            user_input = input("You: ")
            if user_input.lower() == "quit":
                print("Goodbye! Have a nice day!")
                break
            else:
                response = chatbot.respond(user_input)
                if response: 
                    print("Bot:", response)
                else: 
                 print("Bot: I'm not sure how to respond to that.")
chat()

