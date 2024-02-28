import openai
import gradio

openai.api_key = "" #TypeYourAPIKEY

# Initial system message
messages = [{"role": "system", "content": "You are a Doctor Who gives Possible Treatment with medicine based on symptoms also suggest precautions"}]

def CustomChatGPT(user_input):
    # Append user input to the messages
    messages.append({"role": "user", "content": user_input})
    
    # Call OpenAI API for Chat Completion
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    
    # Extract assistant's reply
    assistant_reply = response["choices"][0]["message"]["content"]
    
    # Append assistant's reply to the messages
    messages.append({"role": "assistant", "content": assistant_reply})
    
    # Gradio expects only the assistant's reply as the output
    return assistant_reply

# Define the Gradio Interface
demo = gradio.Interface(
    fn=CustomChatGPT,
    inputs=[gradio.Textbox(type="text", placeholder="Type a message...", label="User Input")],
    outputs=[gradio.Textbox(type="text", label="DoctorBot's Reply")],
    title="Health Assitant by Haka",
)

# Launch the Gradio Interface
demo.launch(share=True)
