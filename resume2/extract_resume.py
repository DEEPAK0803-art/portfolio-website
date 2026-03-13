import docx
import os

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

if __name__ == "__main__":
    resume_path = r"c:\Users\deepa\OneDrive\Desktop\resume2\Deepak_Ranjan_Das_Resume-2.docx"
    if os.path.exists(resume_path):
        text = extract_text_from_docx(resume_path)
        with open("resume_text.txt", "w", encoding="utf-8") as f:
            f.write(text)
        print("Successfully extracted resume text to resume_text.txt")
    else:
        print(f"Resume file not found at {resume_path}")
