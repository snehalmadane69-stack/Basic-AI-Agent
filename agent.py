def run_agent(question):

    question = question.lower()

    if "exam" in question or "study" in question:
        return "You should make a study plan and start with important topics."

    elif "rain" in question or "weather" in question:
        return "Take an umbrella and check the weather before going outside."

    elif "hungry" in question or "food" in question:
        return "You should have a healthy meal."

    elif "tired" in question:
        return "Take a short rest and then continue your work."

    elif "python" in question:
        return "Practice Python programs regularly to improve your programming skills."

    else:
        return "I need more information to make a suitable decision."