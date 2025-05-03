def respond(message):
    
    message = message.lower()  

    if "hello" in message or "hi" in message:  
        return "Hello! How can I help you today?"  
    elif "its ok" in message:  # 
        return "It's ok! Are you ok?"  
    elif "goodbye" in message or "bye" in message: 
        return "Bye, have a good day!"  
    else:
        return "Sorry, my IQ is 2."  

def start_bot():
    print("Bot started. Type 'exit' to quit.")  
    while True:
        user_input = input("You: ")  
        if user_input.lower() == "exit":  
            print("Bot: See you later!") 
            break  
        response = respond(user_input) 
        print("Bot:", response)  

if __name__ == "__main__":
    start_bot()  
