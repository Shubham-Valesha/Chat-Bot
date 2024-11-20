import json

# File to store user data
data_file = "user_data.json"

def load_user_data():
    try:
        with open(data_file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_user_data(data):
    with open(data_file, "w") as f:
        json.dump(data, f)

def set_user_name(user_id, name):
    data = load_user_data()
    data[user_id] = name
    save_user_data(data)
    return f"Name updated to {name}!"

def get_user_name(user_id):
    data = load_user_data()
    return data.get(user_id, "Name not set!")
