import chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
chatbot = ChatBot("Chando")
trainer=ListTrainer(chatbot)
trainer.train([
    "Hi","Hi there!",
    "How are you", "Wel, I am fine",
    "what is your name?","My name is Chando",
    "Who Created You", "Hong Hieu",
    "Do you know about machine learning", "My bot know, contact it",
    "Enter email","chatbot@gmail.com",
    "goodbye","Bye"


])

while True:
    query=input("User: ")
    if query=="exit":
        break
    result=chatbot.get_response(query)
    print("Chat: ", result)

