import markdown
from markdown.extensions import tables, toc
import pdfkit

def markdown_to_pdf():
    # Read the markdown file
    with open('GUÍA_COMPLETA_VIAJE_EUROPA_2026.md', 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    
    # Convert markdown to HTML
    html = markdown.markdown(
        markdown_content,
        extensions=['tables', 'toc'],
        tab_length=2
    )
    
    # Add CSS styling
    html_with_style = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Guía Completa Viaje Europa 2026</title>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                line-height: 1.6;
                margin: 40px;
                color: #333;
            }}
            h1 {{
                color: #2c3e50;
                border-bottom: 3px solid #3498db;
                padding-bottom: 10px;
            }}
            h2 {{
                color: #34495e;
                margin-top: 30px;
                border-bottom: 2px solid #ecf0f1;
                padding-bottom: 8px;
            }}
            h3 {{
                color: #5d6d7e;
                margin-top: 25px;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
                font-size: 14px;
            }}
            th, td {{
                border: 1px solid #bdc3c7;
                padding: 12px;
                text-align: left;
            }}
            th {{
                background-color: #3498db;
                color: white;
                font-weight: bold;
            }}
            tr:nth-child(even) {{
                background-color: #f8f9fa;
            }}
            .checkmark {{
                color: #27ae60;
                font-weight: bold;
            }}
            .cross {{
                color: #e74c3c;
                font-weight: bold;
            }}
            ul, ol {{
                margin-left: 20px;
            }}
            li {{
                margin-bottom: 5px;
            }}
            strong {{
                color: #2c3e50;
            }}
            .page-break {{
                page-break-before: always;
            }}
        </style>
    </head>
    <body>
        {html}
    </body>
    </html>
    """
    
    # Save HTML temporarily
    with open('temp_guide.html', 'w', encoding='utf-8') as f:
        f.write(html_with_style)
    
    # Convert to PDF using pdfkit
    try:
        options = {
            'page-size': 'A4',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'no-outline': None,
            'enable-local-file-access': None
        }
        
        pdfkit.from_file('temp_guide.html', 'GUÍA_COMPLETA_VIAJE_EUROPA_2026.pdf', options=options)
        print("✅ PDF generado exitosamente: GUÍA_COMPLETA_VIAJE_EUROPA_2026.pdf")
        
    except Exception as e:
        print(f"❌ Error con pdfkit: {e}")
        print("Intentando con pandoc HTML...")
        
        # Fallback: save as HTML and try pandoc
        pandoc_cmd = 'pandoc temp_guide.html -o "GUÍA_COMPLETA_VIAJE_EUROPA_2026.pdf"'
        import subprocess
        result = subprocess.run(pandoc_cmd, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ PDF generado con pandoc HTML")
        else:
            print(f"❌ Error con pandoc: {result.stderr}")
    
    # Clean up temp file
    import os
    if os.path.exists('temp_guide.html'):
        os.remove('temp_guide.html')

if __name__ == "__main__":
    markdown_to_pdf()