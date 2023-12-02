# Name: Zhaoshan Duan
# Date: 11/30/2023
# Description: 

import gradio
from chatbot import MeowGPT
import config
from User import User

def setup_interace(chatbot):
    interface = gradio.Interface(
            fn=chatbot.create_chat,
            inputs="text",
            outputs="text",
            title="Meow GPT"
    )

    return interface

def launch_host(chatbot):
        audience = User("5001", "meow")

        setup_interace(chatbot).launch(
              auth = (
                   audience.get_username(), 
                   audience.get_password()), 
              auth_message = "Use Course Number for USERNAME. Cat Sound for PASSWORD",
            share=True
        )
        
if __name__ == "__main__":
    chatbot = MeowGPT(config.api_key)
    launch_host(chatbot)