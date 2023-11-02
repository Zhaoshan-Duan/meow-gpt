import openai, gradio, config

openai.api_key = config.api_key
messages = []


def set_system():
    sys_msg = {"role": "system", 
             "content": "You are a veterinarian that specializes in feline health care and cat behaviors."}
    messages.append(sys_msg)    

def generate_response(messages):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages)
    return response
    
def write_messges_to_file(messages):
    pass

def MeowGPT(user_input):
    set_system()
    messages.append({"role": "user", "content": user_input})

    response = generate_response(messages)

    ChatGPT_reply = response["choices"][0]["message"]["content"]

    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

def launch_host():
    demo = gradio.Interface(fn=MeowGPT, inputs = "text", outputs = "text", title = "Meow GPT")
    demo.launch(share=True)

def main():
    launch_host()

main()