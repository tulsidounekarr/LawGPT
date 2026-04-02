
🏛️ Law-GPT – Legal AI Assistant 
 ---
 
💡 Project Objective: Build an AI-powered assistant to help generate, summarize, and analyze legal content efficiently, reducing manual research and improving productivity.

---

🚀 Features:
---
🤖 AI-powered legal assistant for document drafting and summarization
📄 Generate legal drafts, summaries, and insights
🔁 Handles multiple document inputs
📝 Streamlit frontend for interactive use
🔒 Secrets (API keys) safely stored in .env and ignored by Git
🛠️ Tools & Technologies
🐍 Python 3.x
🔗 Groq API – For fast AI inference
🍲 Streamlit – Frontend UI for user interaction
📦 dotenv – To manage secret keys
📄 CSV / File handling – Optional output storage

---

📦 Requirements
---
Python 3.x

---

Install dependencies:
---
pip install -r requirements.txt
Add your .env file with the Groq API key:

---

GROQ_API_KEY=your_api_key_here-
---
▶ How to Run
streamlit run app.py

This will:
---
Launch the Streamlit frontend in your browser
Allow interaction with the AI legal assistant
Generate summaries, drafts, or insights from input text

Preview
---
![image alt](https://github.com/tulsidounekarr/LawGPT/blob/bbba49c9d2c6d9fb9583efbba3253c3000b8b690/WhatsApp%20Image%202026-04-02%20at%202.17.36%20AM.jpegg)

---

📝 Sample Usage:
---
Input: Provide a draft contract for a freelance project.
Output: Generates a professional legal draft with clauses and terms.

---

📂 Project Structure:
---
Law-GPT/
├─ app.py           # Streamlit frontend
├─ main.py          # Core AI logic
├─ requirements.txt # Dependencies
├─ .gitignore       # Ignored files
├─ README.md        # Project documentation
└─ .env             # API key (not tracked)

---

🎯 Hints & Mini Guide:
---
Use streamlit to create interactive frontend components
Use Groq API for AI inference on legal text
Keep sensitive keys in .env
Version control using Git, push to GitHub for collaboration

---

🔑 Key Concepts:
---
AI-assisted legal drafting
Text summarization and analysis
Frontend development with Streamlit
API integration and secret management

💻 GitHub:
---
 [@tulsidounekarr](https://github.com/tulsidounekarr)

📄 License:
---
This project is open-source and available under the MIT License.
