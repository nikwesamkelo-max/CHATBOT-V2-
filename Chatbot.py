memory = {}
conversation_history = []


def learn_fact(key, value):
    memory[key] = value


def get_summary():
    print(
        "Name:", memory.get("name", "Unknown"),
        "| Age:", memory.get("age", "Unknown"),
        "| Mood:", memory.get("mood", "Unknown"),
        "| Favorite Game:", memory.get("favorite_game", "Unknown")
    )


def classify(text):
    text = text.lower()

    if "my name is" in text or "i am" in text or "call me" in text:
        return "save_name"

    elif "i am" in text and "years old" in text:
        return "save_age"

    elif "i am happy" in text or "i am sad" in text:
        return "save_mood"

    elif "favorite game" in text:
        return "save_game"

    elif "tell me about myself" in text:
        return "summary"

    elif "hello" in text or "hi" in text:
        return "greeting"

    else:
        return "unknown"


while True:
    user_input = input("> ")

    # store conversation history
    conversation_history.append(user_input)

    action = classify(user_input)

    # SAVE NAME
    if action == "save_name":
        name = (
            user_input
            .lower()
            .replace("my name is", "")
            .replace("i am", "")
            .replace("call me", "")
            .strip()
            .capitalize()
        )
        learn_fact("name", name)
        print("Nice to meet you,", name)

    # SAVE AGE
    elif action == "save_age":
        age = user_input.lower().replace("i am", "").replace("years old", "").strip()
        learn_fact("age", age)
        print("Got it, you're", age, "years old.")

    # SAVE MOOD
    elif action == "save_mood":
        mood = "happy" if "happy" in user_input.lower() else "sad"
        learn_fact("mood", mood)
        print("Mood updated to", mood)

    # SAVE GAME
    elif action == "save_game":
        game = user_input.lower().replace("my favorite game is", "").strip().upper()
        learn_fact("favorite_game", game)
        print("Nice, I’ll remember that.")

    # SUMMARY
    elif action == "summary":
        get_summary()

    # GREETING
    elif action == "greeting":
        print("Hey 👋 how can I help you?")

    # UNKNOWN
    else:
        print("I don't understand that yet.")
