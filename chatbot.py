from user_storage import set_user_name, get_user_name

def greet_user(user_id):
    name = get_user_name(user_id)
    if name:
        return f"Welcome back, {name}!"
    else:
        return "Hello! What's your name?"

def process_request(user_input, user_id):
    user_input = user_input.lower()

    if "name is" in user_input:
        name = user_input.split("is")[-1].strip()
        return set_user_name(user_id, name)
    
    if "update name to" in user_input:
        name = user_input.split("to")[-1].strip()
        return set_user_name(user_id, name)
    
    if "weather" in user_input:
        return "I can't fetch weather updates right now. Try asking something else!"

    if "how are you" in user_input:
        return "I'm just a bot, but I'm here to help! How can I assist you today?"

    return "I'm sorry, I didn't understand that. Could you rephrase your request?"

def chatbot():
    user_id = "user_1"  # You can replace this with a dynamic user ID system.
    print("AI Chatbot: Welcome!")
    print(greet_user(user_id))

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("AI Chatbot: Goodbye! Have a nice day!")
            break

        response = process_request(user_input, user_id)
        print(f"AI Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
