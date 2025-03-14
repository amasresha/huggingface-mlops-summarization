from transformers import pipeline
import gradio as gr

# Load summarization pipeline with PyTorch backend
summarizer = pipeline(
    "summarization", model="sshleifer/distilbart-cnn-12-6", framework="pt"
)


def summarize_text(text):
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]["summary_text"]


# Gradio interface
def gradio_interface(text):
    return summarize_text(text)


# Create Gradio app
demo = gr.Interface(
    fn=gradio_interface,
    inputs=gr.Textbox(lines=10, placeholder="Enter text block to summarize..."),
    outputs="text",
    title="Text Summarization App",
    description="Summarize long text using Hugging Face Transformers and Gradio.",
)

# Launch the app
if __name__ == "__main__":
    demo.launch()
