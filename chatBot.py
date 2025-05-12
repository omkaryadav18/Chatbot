#import reg exp module to handle pattern matching
import re

#A dictionary to map keywords to predifined responses
responses = {
    "hello": "Hi there! How can I assist you today?",
    "hi": "Hello Omkar! How can I help you?",
    "How are you": "I am doing great! Thanks for asking. How about you?",
    "what is your name": "My name is  GOGO. I am a chatbot created to assist you.",
    "help": "Sure, I'm here to help. What do you need assistance with?",
    "bye": "Goodbye! Have a great day.",
    "thank you": "You're welcome! I'm happy to help.",
    "default": "I'm not sure, caould you please rephrase?"
}

#Func to find appropriet resonse based on user inpt
def chatbot_response(user_input):
    #convert user input to lowercase
    user_input = user_input.lower()

    for keyword in responses:
        if re.search(keyword, user_input):
            return responses[keyword]

    return responses["default"]

#main func to run chatbot
def chatbot():
    print("Chatbot: Hello! I'm here to assist you. (Type 'bye' to exit)")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break

        response = chatbot_response(user_input)

        print(f"Chatbot: {response}")

chatbot()