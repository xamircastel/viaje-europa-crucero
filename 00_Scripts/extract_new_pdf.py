import PyPDF2
import os

def extract_pdf_text(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
        return text
    except Exception as e:
        return f"Error reading {pdf_path}: {str(e)}"

# Extract only the new file
pdf_file = "confirmation_181627043_1.pdf"
print(f"=== NUEVO DOCUMENTO CRUCERO FAMILIA ANNI ===\n")
print(f"--- {pdf_file} ---")
content = extract_pdf_text(pdf_file)
print(content)
print("\n" + "="*80 + "\n")