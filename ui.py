# Name: Zhaoshan Duan
# Date: 11/30/2023
# Description: 

import gradio
from chatbot import MeowGPT
import config

def launch_host(chatbot):
        demo = gradio.Interface(
            fn=chatbot.create_chat,
            inputs="text",
            outputs="text",
            title="Meow GPT"
        )
        demo.launch(share=True)

if __name__ == "__main__":
    chatbot = MeowGPT(config.api_key)
    launch_host(chatbot)