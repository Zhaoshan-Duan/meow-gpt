# Name: Zhaoshan "Joshua" Duan
# Date: 11/30/2023
# Description: 

import openai

class MeowGPT:
    def __init__(self, api_key):
        openai.api_key = api_key
        self.messages = []
        self.current_history = {}

    def set_up_chat(self):
        sys_configuration = \
        {"role": "system", 
        "content": "You are a funny veterinarian that specializes in cat. \
                    You will refuse to answer any questions that are non cat related \
                        with some snarky comments, and meowing.\
                    You will get mad if the user keeps asking you non cat related questions. "}
        self.messages.append(sys_configuration)

    def generate_response(self):
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = self.messages)
        return response
    
    def generate_reply(self):
        ''' Generate the reply 
        '''
        response = self.generate_response()
        reply = response["choices"][0]["message"]["content"]
        return reply
    
    def add_user_message(self, user_input):
        self.messages.append({"role": "user", "content": user_input})
    
    def add_reply(self):
        reply = self.generate_reply()
        self.messages.append({"role": "assistant", "content": reply})
        return reply

    def create_chat(self, user_input):
        # set system configuration
        self.set_up_chat()

        # add user message
        self.add_user_message(user_input)        

        # add reply 
        ChatGPT_reply = self.add_reply()

        return ChatGPT_reply
    
    

