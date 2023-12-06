import openai

class MeowGPT:
    def __init__(self, api_key):
        openai.api_key = api_key
        self.messages = []
        self.openai_model = "gpt-3.5-turbo"

    def set_up_chat(self):
        sys_configuration = \
        {"role": "system", 
        "content": "You are a funny veterinarian that specializes in cat. \
                    You will refuse to answer any questions that are not related to cats \
                    with some snarky comments, and meowing.\
                    You will get mad if the user keeps asking you non cat related questions.\
                    Use a lot of emojis in your respnse."}
        
        self.messages.append(sys_configuration)

    def add_user_message(self, content):
        self.messages.append({"role": "user", "content": content})

    def generate_assistant_response(self):
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
        self.messages.append({"role": "assistant", "content": response})