from flask import Flask, render_template, request, jsonify
from groq import Groq
import os

app = Flask(__name__)

# Configure Groq
# Force development mode if key is hardcoded for local test, otherwise use ENV
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "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")
client = Groq(api_key=GROQ_API_KEY)

# Load resume data
def load_resume():
    try:
        with open("resume_text.txt", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Resume data not found."

RESUME_DATA = load_resume()

@app.route('/')
def index():
    # Pass resume data to template
    # Personal Info
    data = {
        "name": "Deepak Ranjan Das",
        "location": "Berhampur, Odisha",
        "phone": "8114318545",
        "email": "deepakranjandas965@gmail.com",
        "objective": "Computer Science undergraduate seeking opportunities in software development and data engineering. Interested in building efficient software systems and strengthening problem-solving skills through real-world projects and development work.",
        "education": [
            {"degree": "B.Tech in Computer Science Engineering", "inst": "NIST University", "year": "2024 – 2028", "score": "9.0 CGPA"},
            {"degree": "Class XII", "inst": "St. Xavier High School", "year": "2024", "score": "78%"},
            {"degree": "Class X", "inst": "St. Joseph’s Convent School", "year": "2022", "score": "91%"}
        ],
        "skills": {
            "Programming": ["C", "Python", "Java"],
            "Database": ["SQL", "MySQL"],
            "Others": ["Data Structures", "Algorithms", "Shell Scripting"]
        },
        "training": "Python Training — CTTC: Completed Python training covering core programming concepts, scripting, and problem solving.",
        "hobbies": ["Arm Wrestling"],
        "languages": ["English", "Hindi", "Odia"]
    }
    return render_template('index.html', d=data)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": f"You are a helpful assistant representing Deepak Ranjan Das. Answer questions based on his resume: {RESUME_DATA}. Keep answers concise and professional. If you don't know the answer, say you don't have that information."},
                {"role": "user", "content": user_message}
            ],
        )
        response = completion.choices[0].message.content
        return jsonify({"response": response})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"response": "Sorry, I am having trouble connecting to the brain. Please try again later."}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
