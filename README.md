# What Now? 🤔

### Turn messy text into clear next steps.

Ever read an email or announcement and think:

> **"Okay... but what am I actually supposed to do?"**

**What Now?** uses an open-weight AI model to turn messy emails, notices, messages, and documents into a simple, structured overview of **what you need to do, when you need to do it, and who is involved.**

## ✨ What it does

Paste any text and What Now? extracts:

* 📝 **Summary** — What is this about?
* ✅ **Action Items** — What do I need to do?
* 📅 **Deadlines** — When do I need to do it?
* 👥 **People / Organizations** — Who is involved?
* ⚠️ **Important Information** — What shouldn't I miss?

The app also displays a **loading indicator while the AI is processing**, so you know when your request is being analyzed.

## 🚀 Example

### Input

> Hi Ananya, please submit the revised assignment to Prof. Mehta by Monday. Make sure you attach the updated bibliography and send a confirmation to Prof. Mehta once you've submitted it. Also, please fill out the feedback form from the ISI Mathematics Department before Friday. If you have any questions, contact Rahul from the Academic Office.

### Output

**📝 Summary**

Ananya needs to submit a revised assignment with an updated bibliography to Prof. Mehta by Monday and complete the ISI Mathematics Department feedback form by Friday.

**✅ Action Items**

* ☐ Submit the revised assignment to Prof. Mehta
* ☐ Attach the updated bibliography to the assignment
* ☐ Send a confirmation to Prof. Mehta after submission
* ☐ Fill out the feedback form from the ISI Mathematics Department
* ☐ Contact Rahul from the Academic Office if there are questions

**📅 Deadlines**

* **Monday**
* **Friday**

**👥 People / Organizations**

* Ananya
* Prof. Mehta
* ISI Mathematics Department
* Rahul
* Academic Office

**⚠️ Important Information**

* The assignment must include an updated bibliography
* A confirmation must be sent to Prof. Mehta once the assignment is submitted

## 🧠 How It Works

```text
   User
    │
    │  Email / Document / Message
    ▼
┌─────────────────────┐
│      What Now?      │
│       Gradio        │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│      Gemma 4        │
│   Open-weight LLM   │
└──────────┬──────────┘
           │
           ▼
     Structured JSON
           │
           ▼
┌─────────────────────┐
│ Summary             │
│ Action Items        │
│ Deadlines           │
│ People              │
│ Important Info      │
└─────────────────────┘
```

## 🛠️ Built With

* Python
* Gradio
* Google GenAI Python SDK
* **Gemma 4**, an open-weight AI model

## 🔒 Privacy

The application does not store submitted text.

Text is sent to the configured AI model for analysis and the result is displayed in the browser.

**Never commit your API key.** Store it in a local `.env` file.

## 💻 Running Locally

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/what-now.git
cd what-now
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Create a `.env` file:

```text
GEMINI_API_KEY=your_api_key_here
```

Run:

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:7860
```
