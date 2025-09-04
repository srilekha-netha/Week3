# Week3
## Day1_Streamlit_Basics
### Task1_Loan_Calculator_App
An advanced **Streamlit web app** to calculate loan repayments, generate amortization schedules, and visualize results with **interactive Plotly graphs**.  
This project is designed to help users explore loan repayment options, EMI structures, and perform **what-if analyses** with extra payments.
#### Features
User-friendly form to input loan details (Principal, Rate, Duration, Insurance, Extra Payments, Lump Sum)  
Automatic calculation of **EMI (Monthly Payment), Total Interest, Total Repayment**  
Detailed **Amortization Table** with CSV download option  
Interactive Plotly Graphs:
- Loan balance over time (line chart)  
- Principal vs Interest (stacked area chart)  
- Yearly interest payments (bar chart)  
**What-If Analysis** – compare scenarios with and without extra payments  
Clean sidebar navigation & responsive layout
## Demo: https://srilekhanetha.streamlit.app/
---

### Task2_ChatApp_Groq_OpenAI
Debate Partner Bot
A Streamlit-based AI-powered Debate Partner that engages users in debates by taking the **opposite stance** and generating a **neutral conclusion** at the end. Perfect for practicing debating skills, brainstorming ideas, or just having fun discussions.
#### Features
- **Interactive Debate**: Chat with an AI that always argues the opposite point of view.
- **Customizable Debate Style**: Choose from Formal, Casual, Academic, or Friendly styles.
- **Debate Summary**: Automatically generates a short, balanced conclusion after the debate.
- **PDF Export**: Download the entire debate as a PDF transcript.
- **Session Management**: Keeps track of conversation history and user details.
- **Clear History**: Option to reset and start a new debate anytime.
---
## Demo : https://debate-partner-bot.streamlit.app/
<img width="1920" height="1012" alt="screencapture-debate-partner-bot-streamlit-app-2025-08-19-19_36_29" src="https://github.com/user-attachments/assets/3f0044a2-7761-4a25-90f5-4e86a4037f0d" />
---

## Day2_AI_Agent_Basics
### Task1_MultiAgent_RAG_System
#### Multi-Agent RAG Chatbot
This project is a **Streamlit-based Multi-Agent Chatbot** powered by **LangChain + Groq LLM**.  
It allows users to upload **Salary** and **Insurance** documents (`.docx`), and then query them interactively.  
The chatbot uses **BM25 Retriever** for document search and different **agents** to provide domain-specific answers.  
Features
- **Document Management**  
  - Upload Salary and Insurance `.docx` files directly from the sidebar.  
  - View which documents are currently loaded.  
  - Delete existing files and upload new ones.  

- **Multi-Agent Workflow**  
  - **Salary Agent** → Answers salary-related queries.  
  - **Insurance Agent** → Answers insurance-related queries.  
  - **Coordinator Agent** → Combines both responses into a final, concise answer if the query involves both.
 ---

 ## Additional task
 ### Interview Bot
An AI-powered **Interview Assistant** built with **Streamlit**, designed to:
- Parse resumes and extract key information
- Generate personalized interview questions
- Conduct **video interview sessions** with AI-powered audio question prompts
- Provide an **HR FAQ chatbot** for quick answers
#### Features
### 📄 Resume Upload
- Upload **PDF/DOCX resumes**
- Extracts text using `docx2txt` / `pdfminer`
- Automatically generates personalized interview questions
### 🎥 AI Interview
- AI reads out interview questions using **Text-to-Speech (gTTS)**
- Candidate answers via **live video recording**
- **Timer countdown** for each question
- Automatic navigation between questions
- End interview with a summary
### 💬 FAQ Bot
- HR FAQ chatbot trained from `data/hr_faq.txt`
- Answers common HR-related questions instantly
