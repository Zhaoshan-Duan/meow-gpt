# Name: Zhaoshan Duan
# Date: 12/6/2023
# Class: CS 5001
# Description: This class encapsulates ChatGPT model settings
import openai

class MeowGPT:
    '''
        MeowGPT class
    '''
    def __init__(self, api_key):
        '''
            Constructor
        '''
        self.messages = []
        self.openai_model = "gpt-3.5-turbo"
        openai.api_key = api_key

    def set_up_chat(self):
        '''
            Set system configuration
        '''
        sys_configuration = \
        {"role": "system", 
        "content": "You are a funny veterinarian that specializes in cat. \
                    You will refuse to answer any questions that are not related to cats \
                    with some snarky comments, and meowing.\
                    You will get mad if the user keeps asking you non cat related questions.\
                    Use a lot of emojis in your respnse."}
        
        self.messages.append(sys_configuration)

    def add_user_message(self, content):
        ''' 
            Append user message to chat history
        '''
        self.messages.append({"role": "user", "content": content})

    def generate_assistant_response(self):
        '''
            Generate assistant response from OpenAI API
        '''
        full_response = ""

        for response in openai.ChatCompletion.create(
            model = self.openai_model,
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in self.messages
            ],
            stream=True
        ):
            full_response += response.choices[0].delta.get("content", "")
        return full_response
    
    def add_assistant_message(self, response):
        '''
            Append assistange message to chat history
        '''
        self.messages.append({"role": "assistant", "content": response})