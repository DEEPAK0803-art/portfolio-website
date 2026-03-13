from groq import Groq
import os

GROQ_API_KEY = "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"
client = Groq(api_key=GROQ_API_KEY)

try:
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "user", "content": "Hello, how are you?"}
        ],
    )
    print("API Result:", completion.choices[0].message.content)
except Exception as e:
    print(f"Direct API Error: {e}")
