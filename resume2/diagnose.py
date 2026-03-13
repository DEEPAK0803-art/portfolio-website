try:
    from flask import Flask, render_template, request, jsonify
    print("Flask import successful")
except ImportError as e:
    print(f"Flask import failed: {e}")

try:
    from groq import Groq
    print("Groq import successful")
except ImportError as e:
    print(f"Groq import failed: {e}")
except Exception as e:
    print(f"Groq error: {e}")
