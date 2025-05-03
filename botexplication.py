def respond(message):
    # O código dentro da função "respond" precisa ser indentado corretamente
    message = message.lower()  # A mensagem é convertida para minúsculas

    if "hello" in message or "hi" in message:  # Se a mensagem contém "hello" ou "hi"
        return "Hello! How can I help you today?"  # Resposta do bot
    elif "its ok" in message:  # Se a mensagem contém "its ok"
        return "It's ok! Are you ok?"  # Resposta do bot
    elif "goodbye" in message or "bye" in message:  # Se a mensagem contém "goodbye" ou "bye"
        return "Bye, have a good day!"  # Resposta do bot
    else:
        return "Sorry, my IQ is 2."  # Resposta padrão quando o bot não entende

def start_bot():
    print("Bot started. Type 'exit' to quit.")  # Mensagem inicial
    while True:
        user_input = input("You: ")  # Solicita entrada do usuário
        if user_input.lower() == "exit":  # Se o usuário digitar "exit"
            print("Bot: See you later!")  # Mensagem de despedida
            break  # Encerra o loop e o programa
        response = respond(user_input)  # Chama a função respond para gerar a resposta
        print("Bot:", response)  # Exibe a resposta do bot

if __name__ == "__main__":
    start_bot()  # Chama a função start_bot para iniciar o bot