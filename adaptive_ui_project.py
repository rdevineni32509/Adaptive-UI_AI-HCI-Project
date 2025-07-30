import gradio as gr
from textblob import TextBlob

# Memory for chat history
chat_history = []

def chatbot_response(message):
    global chat_history
    sentiment = TextBlob(message).sentiment.polarity

    if sentiment > 0.2:
        response = "Thank you for the positive message. Let me know if you need anything else."
    elif sentiment < -0.2:
        response = "I'm sorry to hear that. Please tell me more so I can assist you."
    else:
        response = "Thank you. Please continue if there's more you'd like to say."

    chat_history.append((message, response))
    return "", chat_history

with gr.Blocks() as demo:
    gr.Markdown("# Adaptive Sentiment Chatbot")
    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="Your Message")
    clear = gr.Button("Clear Chat")

    msg.submit(fn=chatbot_response, inputs=msg, outputs=[msg, chatbot])
    clear.click(lambda: [], None, chatbot)

demo.launch()
