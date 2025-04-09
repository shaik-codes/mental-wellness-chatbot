import gradio as gr

def chatbot_response(message):
    if "sad" in message or "tired" in message:
        return "I'm here for you. Take a break, you've earned it ❤️"
    elif "exam" in message:
        return "No matter how it went, you showed up. That’s courage, bro 💪"
    elif "scared" in message:
        return "It’s okay to feel scared. You’re not alone, and you’ll get through this."
    else:
        return "I'm always here to chat. Tell me more 🙂"

gr.Interface(fn=chatbot_response, inputs="text", outputs="text").launch()
