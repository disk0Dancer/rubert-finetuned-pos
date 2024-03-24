import gradio as gr
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

headers = {"Authorization": f"Bearer {AUTH_TOKEN}"} 

def postproccess(responce):
      return ' '.join(x['entity_group'] for x in responce)

def query(request):
    response = requests.post(API_URL, headers=headers, json=request)
    return postproccess(response.json())
	

with gr.Blocks() as demo:
    gr.Markdown(
    """
    # Модель для определения скелетной структуры текста
    
    Это демо-приожение демонстрирует работу модели.

    - [Репозеторий модели]()
    - [Репозеторий проекта]()

    """)
    inp = gr.Textbox(placeholder="Введите текст на русском языке...", label="input")
    out = gr.Textbox(label="output")
    inp.change(query, inp, out)

if __name__ == "__main__":
    demo.launch(server_port=7860, share=True)#server_name="0.0.0.0"
