def get_response(user_input):
    text = user_input.lower()
    if "hello" in text or "hi" in text:
        return "Hello! How can I assist you today?"
    elif "help" in text:
        return "Sure! What do you need help with?"
    elif "bye" in text or "goodbye" in text:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"
if __name__ == "__main__":
    print("Bot: Hello! I am your assistant. Type 'exit' or 'quit' to stop.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the chat. Goodbye!")
            break
        response = get_response(user_input)
        print("Bot:", response)
        