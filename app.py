import os
import json

import gradio as gr
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def analyze(text):
    if not text.strip():
        return "Please paste some text first."

    prompt = f"""
You are What Now?, an assistant that turns messy text into
clear, actionable information.

Analyze the text below and return ONLY valid JSON.
Do not use Markdown or code fences.

Use exactly this structure:

{{
  "summary": "A concise 1-3 sentence summary.",
  "action_items": ["thing to do 1", "thing to do 2"],
  "deadlines": ["deadline 1", "deadline 2"],
  "people": ["person or organization 1"],
  "important_information": ["important point 1", "important point 2"]
}}

Rules:
- Do not invent information.
- If there are no action items, return an empty list.
- If there are no deadlines, return an empty list.
- If there are no people or organizations, return an empty list.
- If there is no important information, return an empty list.

TEXT:
{text}
"""

    try:
        response = client.models.generate_content(
            model="gemma-4-26b-a4b-it",
            contents=prompt,
        )
    except Exception:
        return (
            "⚠️ **The AI service encountered an error.**\n\n"
            "Please try again in a moment."
        )

    try:
        data = json.loads(response.text)
    except (json.JSONDecodeError, TypeError):
        return (
            "⚠️ **I couldn't understand the AI response.**\n\n"
            "Please try again."
        )

    result = f"## 📝 Summary\n\n{data['summary']}\n\n"

    result += "## ✅ Action Items\n\n"

    if data["action_items"]:
        result += "\n".join(
            f"- ☐ {item}" for item in data["action_items"]
        )
    else:
        result += "No action items identified."

    result += "\n\n## 📅 Deadlines\n\n"

    if data["deadlines"]:
        result += "\n".join(
            f"- **{deadline}**" for deadline in data["deadlines"]
        )
    else:
        result += "No deadlines identified."

    result += "\n\n## 👥 People / Organizations\n\n"

    if data["people"]:
        result += "\n".join(
            f"- {person}" for person in data["people"]
        )
    else:
        result += "None identified."

    result += "\n\n## ⚠️ Important Information\n\n"

    if data["important_information"]:
        result += "\n".join(
            f"- {info}" for info in data["important_information"]
        )
    else:
        result += "None identified."

    return result


CSS = """
#title {
    text-align: center;
    margin-bottom: 0.25rem;
}

#subtitle {
    text-align: center;
    opacity: 0.7;
    margin-bottom: 2rem;
}

#input-box textarea {
    font-size: 15px !important;
}

#analyze-button {
    width: 100%;
    margin-top: 10px;
}

#result {
    margin-top: 25px;
}
"""


with gr.Blocks(
    title="What Now?",
    theme=gr.themes.Soft(),
    css=CSS,
) as app:

    gr.Markdown(
        """
        # What Now? 🤔
        """,
        elem_id="title",
    )

    gr.Markdown(
        """
        ### Turn messy emails, notices, and messages into clear next steps.
        """,
        elem_id="subtitle",
    )

    with gr.Row():

        with gr.Column(scale=1):

            text_input = gr.Textbox(
                label="Paste your text",
                placeholder=(
                    "Paste an email, announcement, message, "
                    "or document here..."
                ),
                lines=14,
                elem_id="input-box",
            )

            analyze_button = gr.Button(
                "✨ What Now?",
                variant="primary",
                elem_id="analyze-button",
            )

        with gr.Column(scale=1):

            output = gr.Markdown(
                value=(
                    "### 👋 Ready when you are!\n\n"
                    "Paste something on the left and click "
                    "**What Now?** to find out what needs your attention."
                ),
                elem_id="result",
            )

    analyze_button.click(
        fn=analyze,
        inputs=text_input,
        outputs=output,
        show_progress="full",
    )


if __name__ == "__main__":
    app.launch()
