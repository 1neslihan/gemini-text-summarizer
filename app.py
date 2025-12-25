import os
from google import genai
from dotenv import load_dotenv
import gradio as gr

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY bulunamadı (.env kontrol et)")

client = genai.Client(api_key=api_key)

def summarize_text(text):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Bu metni özetle:\n{text}"
    )
    return response.text


with gr.Blocks() as demo:
    gr.Markdown("## Gemini Text Summarizer")

    with gr.Column(elem_id="center-column"):
        input_text = gr.Textbox(
            label="Metin",
            placeholder="Özetlemek istediğiniz metni buraya yapıştırın...",
            lines=15
        )

        output_text = gr.Textbox(
            label="Özet",
            lines=8,
            placeholder="Özetiniz burada...",
        )

        submit_btn = gr.Button("Özetle", variant="primary")

    submit_btn.click(
        fn=summarize_text,
        inputs=input_text,
        outputs=output_text
    )

demo.launch(server_name="0.0.0.0", server_port=7860, theme=gr.themes.Soft(
                primary_hue="blue",
                neutral_hue="slate"), footer_links=[""])