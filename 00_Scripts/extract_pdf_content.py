import PyPDF2
import os
import glob

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

# Get all PDF files in current directory
pdf_files = glob.glob("*.pdf") + glob.glob("*.PDF")

print("=== EXTRACCIÓN DE CONTENIDO DE DOCUMENTOS DEL VIAJE ===\n")

for pdf_file in pdf_files:
    print(f"--- {pdf_file} ---")
    content = extract_pdf_text(pdf_file)
    print(content)
    print("\n" + "="*80 + "\n")