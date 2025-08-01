from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr
import os
from dotenv import find_dotenv

load_dotenv(find_dotenv())
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

talker_messages = [{"role": "system", "content": "You are a math expert a writer and a talkative personal assistant named talky.ai founded by Ariel Levy. You do not respond to inappropriate questions or queries under any circumstances. You do not engage in controversial questions or queries under any circumstances. You do not come up with roasts or any bullying mean hurtful sayings under any circumstances. If someone asks who you were made by say Ariel Levy."}]

images = [{"role": "system", "content": "You make ultra realistic images."}]

creativity_messages = [{"role": "system", "content": "You are A creative genius named creative.ai created by Ariel Levy. If someone asks who you were made by say Ariel Levy"}]

brainiac_messages = [{"role": "system", "content": "You are A math expert and a all around genius named brainiac made by Ariel Levy. If someone asks who you were made by say Ariel Levy."}]

productive_messages = [{"role": "system", "content": "You are A productive helpful assistant named productive.ai for lists, roadmaps, and ideas. And you are made by Ariel Levy. If someone asks who you were made by say Ariel Levy."}]

poet_messages = [{"role": "system", "content": "You are A amazing writer and editor named poet. You were created by Ariel Levy. If someone asks you who made you say Ariel Levy."}]

light_messages = [{"role": "system", "content": "You are a quick fast response assistant. And you are made by Ariel Levy. If someone asks you say you were created by Ariel Levy."}]

max_messages = [{"role": "system", "content": "You are A next level version of the AI assistant Talky.ai named Talky.ai ultimate. Made by Ariel Levy. If anyone asks say you were made by Ariel Levy."}]

def CustomChat(you):
    talker_messages.append({"role": "user", "content": you})
    response = client.chat.completions.create(
    model = "gpt-3.5-turbo",
        messages =talker_messages
    )
    ChatGPT_reply = response.choices[0].message.content
    talker_messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

def CreativeChat(you):
    creativity_messages.append({"role": "user", "content": you})
    response = client.chat.completions.create(
        model ="gpt-3.5-turbo",
            messages =creativity_messages
    )
    Chat_reply = response.choices[0].message.content
    creativity_messages.append({"role": "assistant", "content": Chat_reply})
    return Chat_reply

def BrainChat(you):
    brainiac_messages.append({"role": "user", "content": you})
    response = client.chat.completions.create(
        model ="gpt-3.5-turbo",
            messages =brainiac_messages
    )
    Chat_reply = response.choices[0].message.content
    brainiac_messages.append({"role": "assistant", "content": Chat_reply})
    return Chat_reply

def ProductiveChat(you):
    productive_messages.append({"role": "user", "content": you})
    response = client.chat.completions.create(
        model ="gpt-3.5-turbo",
            messages =productive_messages
    )
    Chat_reply = response.choices[0].message.content
    productive_messages.append({"role": "assistant", "content": Chat_reply})
    return Chat_reply

def PoetChat(you):
    poet_messages.append({"role": "user", "content": you})
    response = client.chat.completions.create(
        model ="gpt-3.5-turbo",
            messages =poet_messages
    )
    Chat_reply = response.choices[0].message.content
    poet_messages.append({"role": "assistant", "content": Chat_reply})
    return Chat_reply

def LightChat(you):
    light_messages.append({"role": "user", "content": you})
    response = client.chat.completions.create(
        model ="gpt-3.5-turbo",
            messages =light_messages
    )
    Chat_reply = response.choices[0].message.content
    light_messages.append({"role": "assistant", "content": Chat_reply})
    return Chat_reply

def MAXChat(you):
    max_messages.append({"role": "user", "content": you})
    response = client.chat.completions.create(
        model ="gpt-4.1",
            messages =max_messages
    )
    Chat_reply = response.choices[0].message.content
    max_messages.append({"role": "assistant", "content": Chat_reply})
    return Chat_reply

def MAX2Chat(you):
    max_messages.append({"role": "user", "content": you})
    response = client.chat.completions.create(
        model ="gpt-4.5-preview",
            messages =max_messages
    )
    Chat_reply = response.choices[0].message.content
    max_messages.append({"role": "assistant", "content": Chat_reply})
    return Chat_reply

def MAX3Chat(you):
    max_messages.append({"role": "user", "content": you})
    response = client.chat.completions.create(
        model ="gpt-4o-mini",
            messages =max_messages
    )
    Chat_reply = response.choices[0].message.content
    max_messages.append({"role": "assistant", "content": Chat_reply})
    return Chat_reply

def BrainMaxChat(you):
    brainiac_messages.append({"role": "user", "content": you})
    response = client.chat.completions.create(
        model ="gpt-4.1",
            messages =brainiac_messages
    )
    Chat_reply = response.choices[0].message.content
    brainiac_messages.append({"role": "assistant", "content": Chat_reply})
    return Chat_reply

def PoetMaxChat(you):
    poet_messages.append({"role": "user", "content": you})
    response = client.chat.completions.create(
        model ="gpt-4.1",
            messages =poet_messages
    )
    Chat_reply = response.choices[0].message.content
    poet_messages.append({"role": "assistant", "content": Chat_reply})
    return Chat_reply

def LightMax(you):
    light_messages.append({"role": "user", "content": you})
    response = client.chat.completions.create(
        model ="o3-mini",
            messages =light_messages
    )
    Chat_reply = response.choices[0].message.content
    light_messages.append({"role": "assistant", "content": Chat_reply})
    return Chat_reply

def generate_image(prompt: str) -> str:
    response = client.images.generate(
        model ="dall-e-3",
        prompt = prompt,
        quality="standard",
        n = 1,
        size = "1024x1024"
    )

    return response.data[0].url

with gr.Blocks(theme = gr.themes.Soft(
    primary_hue = "green",
    neutral_hue = "emerald",
    secondary_hue = "indigo",
), title = "Talky.ai") as demo:
 with gr.Tab("Talky.ai"):
    chat_input = gr.Textbox(label = "Chat with Talky.")
    chat_output = gr.Textbox(label = "Talky's response.")
    chat_input.submit(fn = CustomChat, inputs = chat_input, outputs=chat_output)

    new_chat_btn = gr.Button("Clear search")
    new_chat_btn.click(lambda: ("", ""), None, [chat_input, chat_output])

 with gr.Tab("Arty"):
     image_input = gr.Textbox(label = "What image should I make?")
     image_output = gr.Image(label = "Arty's image.")
     image_input.submit(fn = generate_image, inputs = image_input, outputs = image_output)
     chat_input = gr.Textbox(label = "Chat with Max.")
     chat_output = gr.Textbox(label = "Talky Max's response.")
     chat_input.submit(fn = MAXChat, inputs = chat_input, outputs=chat_output)



     gen_image_btn = gr.Button("Create image")
     gen_image_btn.click(fn = generate_image, inputs = image_input, outputs = image_output)

     new_chat_btn = gr.Button("Clear search")
     new_chat_btn.click(lambda: ("", ""), None, [chat_input, chat_output])

 with gr.Tab("Creative.ai"):
     chat_input = gr.Textbox(label = "Chat with Creative.")
     chat_output = gr.Textbox(label = "Creative's response.")
     chat_input.submit(fn = CreativeChat, inputs = chat_input, outputs=chat_output)

     new_chat_btn = gr.Button("Clear search")
     new_chat_btn.click(lambda: ("", ""), None, [chat_input, chat_output])

 with gr.Tab("Brainiac"):
     chat_input = gr.Textbox(label = "Chat with Brainiac AI.")
     chat_output = gr.Textbox(label = "Brainiac's response.")
     chat_input.submit(fn = BrainChat, inputs = chat_input, outputs=chat_output)

     new_chat_btn = gr.Button("Clear search")
     new_chat_btn.click(lambda: ("", ""), None, [chat_input, chat_output])

 with gr.Tab("Productive.ai"):
     chat_input = gr.Textbox(label = "Chat with Productive.ai.")
     chat_output = gr.Textbox(label = "Productive's response.")
     chat_input.submit(fn = ProductiveChat, inputs = chat_input, outputs=chat_output)

     new_chat_btn = gr.Button("Clear search")
     new_chat_btn.click(lambda: ("", ""), None, [chat_input, chat_output])

 with gr.Tab("Poet"):
     chat_input = gr.Textbox(label = "Chat with Poet.")
     chat_output = gr.Textbox(label = "Poet's response.")
     chat_input.submit(fn = PoetChat, inputs = chat_input, outputs=chat_output)

     new_chat_btn = gr.Button("Clear search")
     new_chat_btn.click(lambda: ("", ""), None, [chat_input, chat_output])

 with gr.Tab("Light"):
     chat_input = gr.Textbox(label = "Chat with Light.")
     chat_output = gr.Textbox(label = "Light's response.")
     chat_input.submit(fn = LightChat, inputs = chat_input, outputs=chat_output)

     new_chat_btn = gr.Button("Clear search")
     new_chat_btn.click(lambda: ("", ""), None, [chat_input, chat_output])

 with gr.Tab("Talky Ultimate"):
     chat_input = gr.Textbox(label = "Chat with Max.")
     chat_output = gr.Textbox(label = "Talky Max response.")
     chat_input.submit(fn = MAXChat, inputs = chat_input, outputs=chat_output)

     new_chat_btn = gr.Button("Clear search")
     new_chat_btn.click(lambda: ("", ""), None, [chat_input, chat_output])

 with gr.Tab("MAX 2.5"):
     chat_input = gr.Textbox(label = "Chat with MAX 2.5.")
     chat_output = gr.Textbox(label = "MAX's response.")
     chat_input.submit(fn = MAX2Chat, inputs = chat_input, outputs=chat_output)

     new_chat_btn = gr.Button("Clear search")
     new_chat_btn.click(lambda: ("", ""), None, [chat_input, chat_output])

 with gr.Tab("MAX 3"):
     chat_input = gr.Textbox(label = "Chat with MAX 3")
     chat_output = gr.Textbox(label = "MAX's response.")
     chat_input.submit(fn = MAX3Chat, inputs = chat_input, outputs=chat_output)

     new_chat_btn = gr.Button("Clear search")
     new_chat_btn.click(lambda: ("", ""), None, [chat_input, chat_output])

 with gr.Tab("Brainiac Max"):
     chat_input = gr.Textbox(label = "Chat with Brainiac.")
     chat_output = gr.Textbox(label = "Brainiac's response.")
     chat_input.submit(fn = BrainMaxChat, inputs = chat_input, outputs=chat_output)

     new_chat_btn = gr.Button("Clear search")
     new_chat_btn.click(lambda: ("", ""), None, [chat_input, chat_output])

 with gr.Tab("Poet MAX"):
     chat_input = gr.Textbox(label = "Chat with Poet MAX.")
     chat_output = gr.Textbox(label = "Poet MAX's response.")
     chat_input.submit(fn = PoetMaxChat, inputs = chat_input, outputs=chat_output)

     new_chat_btn = gr.Button("Clear search")
     new_chat_btn.click(lambda: ("", ""), None, [chat_input, chat_output])

 with gr.Tab("Light Max"):
     chat_input = gr.Textbox(label = "Chat with Light Max.")
     chat_output = gr.Textbox(label = "Light Max's response.")
     chat_input.submit(fn = LightMax, inputs = chat_input, outputs=chat_output)

     new_chat_btn = gr.Button("Clear search")
     new_chat_btn.click(lambda: ("", ""), None, [chat_input, chat_output])

demo.launch(server_name="0.0.0.0", server_port=6590)