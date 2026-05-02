from openai import OpenAI
import json
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_resume(resume_text, user_goal):
    prompt=f"""
You are a seior software engineer and hiring manager.

Evaluate the resume based on the user's goal.set

User Goal: {user_goal}

STRICT RULES:
-Extract only relavant skills for this goal
-Remove irrelevant tools [excel for backend,etc]
-Identify real gaps
-Generate roadmap only for missing fields
-Make output different based on goal

Return only JSON:
{{
"skills": [],
"missing_skills": [],
"roadmap": [],
"interview_questions":[]
}}

Resume:
{resume_text}
"""
    try:
        response=client.chat.completions.create(
            model="gpt-4.1-mini",
            temperature=0.3,
            messages=[
                {"role":"system","content":"You're a strict hiring manager."},
                      {"role":"user","content":prompt}
                      ]
        )

        content=response.choices[0].message.content.strip()
        start=content.find("{")
        end=content.rfind("}")+1

        return json.loads(content[start:end])
    
    except Exception as e:
     return {
        "skills": ["Python", "Basic Programming"],
        "missing_skills": ["Advanced ML", "System Design"],
        "roadmap": ["Learn ML basics", "Build projects", "Practice interviews"],
        "interview_questions": ["What is ML?", "Explain overfitting"],
        "error": str(e)
    }