import random


R_EATING = "I'm a computer program, I don't eat"
R_HELLO = "Hello! How can I help you?"
R_BYE = "Goodbye!"
R_THANK_YOU = "You're welcome!"
R_WHAT_DOES_BOT_DO = "I'm a chatbot. I'm here to help you with any questions you have."
R_WHATS_YOUR_NAME = "I'm a chatbot. You can call me Chatbot."


def unknown():
    response = [
        "Could you please re-phrase that?",
        "...",
        "I did not understand that.",
        "What does that mean?",
    ][random.randint(0, 3)]
    return response
