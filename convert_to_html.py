import markdown
from markdown.extensions import tables, toc

def markdown_to_html():
    # Read the markdown file
    with open('GUÍA_COMPLETA_VIAJE_EUROPA_2026.md', 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    
    # Convert markdown to HTML
    html = markdown.markdown(
        markdown_content,
        extensions=['tables', 'toc'],
        tab_length=2
    )
    
    # Add CSS styling for better PDF appearance
    html_with_style = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Guía Completa Viaje Europa 2026 - Familia Castelblanco</title>
        <style>
            @page {{
                size: A4;
                margin: 2cm;
            }}
            body {{
                font-family: 'Arial', sans-serif;
                line-height: 1.4;
                color: #333;
                font-size: 12px;
            }}
            h1 {{
                color: #1e3a8a;
                font-size: 24px;
                text-align: center;
                border-bottom: 3px solid #3b82f6;
                padding-bottom: 15px;
                margin-bottom: 25px;
                page-break-after: avoid;
            }}
            h2 {{
                color: #1e40af;
                font-size: 18px;
                margin-top: 25px;
                margin-bottom: 15px;
                border-bottom: 2px solid #dbeafe;
                padding-bottom: 8px;
                page-break-after: avoid;
            }}
            h3 {{
                color: #1e40af;
                font-size: 14px;
                margin-top: 20px;
                margin-bottom: 10px;
                page-break-after: avoid;
            }}
            h4 {{
                color: #374151;
                font-size: 13px;
                margin-top: 15px;
                margin-bottom: 8px;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 15px 0;
                font-size: 10px;
                page-break-inside: avoid;
            }}
            th, td {{
                border: 1px solid #d1d5db;
                padding: 8px 6px;
                text-align: left;
                vertical-align: top;
            }}
            th {{
                background-color: #3b82f6;
                color: white;
                font-weight: bold;
                font-size: 10px;
            }}
            tr:nth-child(even) {{
                background-color: #f8fafc;
            }}
            ul, ol {{
                margin: 10px 0 10px 20px;
                padding: 0;
            }}
            li {{
                margin-bottom: 4px;
                font-size: 11px;
            }}
            strong {{
                color: #1f2937;
            }}
            .emoji {{
                font-size: 14px;
            }}
            p {{
                margin: 8px 0;
                text-align: justify;
            }}
            hr {{
                border: none;
                height: 2px;
                background: linear-gradient(to right, #3b82f6, #93c5fd, #3b82f6);
                margin: 20px 0;
            }}
            .page-break {{
                page-break-before: always;
            }}
            .no-break {{
                page-break-inside: avoid;
            }}
        </style>
    </head>
    <body>
        {html}
        <div class="page-break"></div>
        <p style="text-align: center; color: #6b7280; font-size: 10px; margin-top: 50px;">
            <strong>Documento generado el 18 de Enero 2026</strong><br>
            Para uso exclusivo de la familia Castelblanco en su viaje a Europa<br>
            ¡Buen viaje! 🌍✈️
        </p>
    </body>
    </html>
    """
    
    # Save as HTML file
    with open('GUÍA_COMPLETA_VIAJE_EUROPA_2026.html', 'w', encoding='utf-8') as f:
        f.write(html_with_style)
    
    print("✅ Archivo HTML generado: GUÍA_COMPLETA_VIAJE_EUROPA_2026.html")
    print("📌 Puedes abrir este archivo en cualquier navegador web")
    print("📌 Para convertir a PDF: Abre en Chrome/Edge → Imprimir → Guardar como PDF")
    print("📌 Configuración recomendada: Tamaño A4, márgenes normales, incluir gráficos")

if __name__ == "__main__":
    markdown_to_html()