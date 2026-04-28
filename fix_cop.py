import re
with open('g:\\Mi unidad\\Personal\\Viaje a Europa\\GUÍA_COMPLETA_VIAJE_EUROPA_2026.md', 'r', encoding='utf-8') as f:
 text=f.read()
text=text.replace('.497 COP', '\.497 COP')
text=text.replace('.713', '\.713')
text=text.replace('.784', '\.784')
text=text.replace('.327.200 COP', '\.327.200 COP')
with open('g:\\Mi unidad\\Personal\\Viaje a Europa\\GUÍA_COMPLETA_VIAJE_EUROPA_2026.md', 'w', encoding='utf-8') as f:
 f.write(text)