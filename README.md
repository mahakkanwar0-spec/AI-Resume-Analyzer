# AI Resume Analyzer 🚀

A web-based application that analyzes resumes and provides personalized insights including skills, missing skills, roadmap, and interview questions.

## 🔥 Features

- Upload resume (PDF / DOCX)
- Extract and analyze resume content
- Identify relevant skills based on user goal
- Suggest missing skills and improvement roadmap
- Generate interview questions
- User authentication (Login / Signup)
- History tracking of previous analyses

---

## 🛠 Tech Stack

- Backend: Flask (Python)
- Frontend: HTML, CSS
- Database: SQLAlchemy
- File Handling: PyPDF2, python-docx
- AI Integration: OpenAI API
- Version Control: Git & GitHub

---

## ⚙️ How It Works

1. User uploads resume or pastes text
2. System extracts content
3. AI analyzes resume (if API available)
4. Otherwise fallback logic is used
5. Results are displayed and stored in history

---

## ⚠️ Note

If the OpenAI API is unavailable, the system returns a default response to ensure the application does not break.

---

## 🚀 Run Locally

```bash
git clone https://github.com/mahakkanwar0-spec/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer

pip install -r requirements.txt
python app.py
