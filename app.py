import gradio as gr


def hello(name: str) -> str:
    return f"Hello, {name}!"


gr.Interface(
    fn=hello,
    inputs="text",
    outputs="text",
).launch()
