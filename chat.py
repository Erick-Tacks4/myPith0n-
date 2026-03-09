#Dictionary of predefined questions and answers
response = {
    "hello":"Hi how can i help you today?",
    "how are you":"I'm just a bot but I'm doing fine",
    "okay":"Was that all, or do you stil need some help",
    "yes":"I can help you answer some of the questions you might have. What exactly do you want me to do for you?",
    "i don't know":"Never mind. But I'm always available as long as you need me",
    "what is your name":"I'm ChatPy, your friendly Chatbot!",
    "no":"Okay. See you again next time",
    "mmmh":"Yeah!!! Certainly",
    "no thank you":"Okay. See you again next time",
    "bye":"Okay Good bye! See you again next time have great day ahead!"
}

#Start chating
print("ChatBot: Hey there! Type something to start chatting(Type 'bye' to exit)")

while True:
# Starts an infinite loop to keep the conversation going until the user types "bye".

  user_input = input("You: ").lower()
  if user_input == "bye"or user_input == "nothing":
    print("ChatBot:", response["bye"])
    break
  
  elif user_input == "no" or user_input == "no thank you":
    print("ChatBot:", response["no"])
    break
  
  elif user_input in response:
    print("ChatBot:", response[user_input])

  else:
    print("ChatBot: I'm sorry I don't understand that")