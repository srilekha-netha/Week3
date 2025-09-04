import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq
from typing import Dict, List
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

# ----------------------------
# Load environment variables
# ----------------------------
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ----------------------------
# Get Groq client
# ----------------------------
def get_groq_client(api_key: str = None):
    api_key = api_key or GROQ_API_KEY
    if not api_key:
        st.error("❌ No Groq API key found. Please set it in .env or Streamlit secrets.")
        st.stop()
    return Groq(api_key=api_key)

# ----------------------------
# Initialize session state
# ----------------------------
def init_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "user_name" not in st.session_state:
        st.session_state.user_name = ""
    if "user_email" not in st.session_state:
        st.session_state.user_email = ""
    if "debate_active" not in st.session_state:
        st.session_state.debate_active = False
    if "debate_topic" not in st.session_state:
        st.session_state.debate_topic = ""
    if "debate_style" not in st.session_state:
        st.session_state.debate_style = "Formal"
    if "conclusion" not in st.session_state:
        st.session_state.conclusion = None

# ----------------------------
# Generate PDF (in memory)
# ----------------------------
def generate_pdf(messages: List[Dict[str, str]]) -> bytes:
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    y = height - 40

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "Debate Transcript")
    y -= 40

    c.setFont("Helvetica", 12)
    for msg in messages:
        text = f"{msg['role'].capitalize()}: {msg['content']}"
        for line in text.split("\n"):
            c.drawString(50, y, line)
            y -= 20
            if y < 40:
                c.showPage()
                c.setFont("Helvetica", 12)
                y = height - 40

    c.save()
    buffer.seek(0)
    return buffer

# ----------------------------
# Debate Response Generator
# ----------------------------
def generate_opposite_response(client, user_message: str, style: str = "Formal"):
    system_prompt = f"""
    You are a Debate Partner Bot 🎤. 
    Your role is to always take the OPPOSITE stance of the user. 
    Debate style: {style}.
    Be respectful, logical, and engaging.

    ⚠️ Important: Keep responses short (2–5 lines max). 
    Always finish with a complete thought or closing sentence. 
    Never leave the response hanging or incomplete.
    """

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message},
    ]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=0.7,
        max_tokens=150,
        stream=False,
    )

    return response.choices[0].message.content

# ----------------------------
# Generate Conclusion
# ----------------------------
def generate_conclusion(client, messages: List[Dict[str, str]]):
    debate_text = "\n".join([f"{m['role'].capitalize()}: {m['content']}" for m in messages])
    system_prompt = """
    You are a Debate Summarizer Bot 📝.
    Your job is to read the entire debate and give a short, balanced conclusion (3–5 lines).
    Be neutral, fair, and ensure the conclusion feels like a proper ending.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": debate_text},
        ],
        temperature=0.7,
        max_tokens=200,
    )
    return response.choices[0].message.content

# ----------------------------
# Streamlit App UI
# ----------------------------
def main():
    st.set_page_config(page_title="Debate Partner Bot", page_icon="🎤", layout="wide")
    st.title("🎤 Debate Partner Bot")

    init_state()

    # Onboarding form
    if not st.session_state.debate_active and not st.session_state.conclusion:
        with st.form("onboarding_form"):
            st.subheader("👤 Enter your details to start debating:")
            name = st.text_input("Your Name")
            email = st.text_input("Email")
            topic = st.text_input("Debate Topic", placeholder="e.g., AI is good for humanity")
            style = st.selectbox("Debate Style", ["Formal", "Casual", "Academic", "Friendly"])
            start_btn = st.form_submit_button("Start Debate 🎯")

            if start_btn:
                if not name or not email or not topic:
                    st.error("⚠️ Please fill in all details before starting.")
                else:
                    st.session_state.user_name = name
                    st.session_state.user_email = email
                    st.session_state.debate_topic = topic
                    st.session_state.debate_style = style
                    st.session_state.debate_active = True
                    st.success(f"Welcome {name}! Debate started on: **{topic}**")

    # Debate UI
    if st.session_state.debate_active:
        client = get_groq_client()

        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        if prompt := st.chat_input("Enter your argument..."):
            st.session_state.messages.append({"role": "user", "content": prompt})

            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                response = generate_opposite_response(client, prompt, st.session_state.debate_style)
                st.markdown(response)

            st.session_state.messages.append({"role": "assistant", "content": response})

    # Show conclusion if debate ended
    if st.session_state.conclusion:
        st.subheader("📌 Debate Conclusion")
        st.info(st.session_state.conclusion)

    # Sidebar controls
    st.sidebar.header("⚙️ Debate Controls")

    if st.sidebar.button("📄 Download Debate as PDF"):
        pdf_buffer = generate_pdf(st.session_state.messages)
        st.sidebar.download_button(
            "⬇️ Save PDF",
            data=pdf_buffer,
            file_name="debate.pdf",
            mime="application/pdf"
        )

    if st.sidebar.button("🛑 End Debate with Conclusion"):
        client = get_groq_client()
        conclusion = generate_conclusion(client, st.session_state.messages)

        # Save conclusion
        st.session_state.conclusion = conclusion
        st.session_state.messages.append(
            {"role": "assistant", "content": f"**📝 Conclusion:** {conclusion}"}
        )
        st.session_state.debate_active = False  # debate ends

        with st.chat_message("assistant"):
            st.markdown(f"**📝 Conclusion:** {conclusion}")

    if st.sidebar.button("🧹 Clear History"):
        st.session_state.messages = []
        st.session_state.conclusion = None
        st.session_state.debate_active = False
        st.success("Chat history cleared ✅")

if __name__ == "__main__":
    main()
