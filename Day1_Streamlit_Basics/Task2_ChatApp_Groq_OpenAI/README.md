# 🎤 Debate Partner Bot (Groq + Streamlit)

An interactive **opposite-stance debate bot** built with **Streamlit** and the **Groq LLM API**.  
Features **chat UI**, **session memory**, **live streaming responses**, **clear history**, **end debate with a conclusion**, and **download transcript as PDF**.

## ✨ Features
- Opposite stance bot (argument rebuttal)
- Streamlit chat interface (`st.chat_message`, `st.chat_input`)
- Conversation **session state** persistence
- **Streaming** replies via Groq
- **Clear history** (keep user details) and **Reset All**
- **End Debate** → generates a neutral **conclusion**
- **Download PDF** transcript (includes user details and conclusion)

## 🚀 Quickstart
1. **Clone** or download this project.
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set API key** (choose one):
   - Put your key in environment:
     ```bash
     export GROQ_API_KEY="gsk_..."
     ```
   - Or create `.streamlit/secrets.toml`:
     ```toml
     GROQ_API_KEY="gsk_..."
     ```
   - Or paste it in the app sidebar (masked).

4. **Run the app:**
   ```bash
   streamlit run app.py
   ```

## 🧠 Models
Default model: `llama-3.1-70b-versatile` (sidebar lets you switch to `llama-3.1-8b-instant`).

## 📝 Notes
- The bot **always** argues the opposite stance (via system prompts).
- **Conclusion** is neutral and concise (≤ 180 words).
- PDF export uses **ReportLab**.

## 🧹 Troubleshooting
- If you see **Missing GROQ_API_KEY**, set it via env/secrets/side bar.
- For Streamlit Cloud, set secret under **Settings → Secrets**.

## 📄 License
MIT
