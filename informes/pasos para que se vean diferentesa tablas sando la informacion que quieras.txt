import pandas as pd 
import webbrowser
import os 
from pathlib import Path

#1) Leer el archivo CSV 
df =pd.read_csv('datos_ventas.csv')

#2) ORDENAR por importes de forma DESCENDENTE 
df_ordenado_importe = df.sort_values(by=['Mes', 'Importe'], ascending=[True, False])

print(df_ordenado_importe)

#3)Filtar por el nombre de maximo 
df_filtrado_nombre = df[df['Comercial'] == 'Máximo']

print(df_filtrado_nombre)

#4)Filtar por importes mayores a 3000
df_filtrado_importe = df[df['Importe'] > 3000]

#Filtro
df_filtro_and = df[(df['Mes'] =='Marzo') & (df['Importe'] > 3000)]

# 7) Convertimos a HTML (tablas)
tabla_original = df.to_html(index=False)
tabla_ordenada = df_ordenado_importe.to_html(index=False)
tabla_filtrada = df_filtrado_importe.to_html(index=False)
 
# 8) Montamos HTML final
html = f"""
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Informe 02 - Ordenación y Filtrado</title>
<style>
    body {{ font-family: Arial; margin: 30px; }}
    table {{ border-collapse: collapse; width: 100%; margin: 15px 0; }}
    th, td {{ border: 1px solid #ddd; padding: 8px; }}
    th {{ background: #f2f2f2; }}
    h1 {{ margin-bottom: 0; }}
    p {{ color: #555; margin-top: 5px; }}
</style>
</head>
<body>
<h1>Informe 02 - Ordenación y Filtrado</h1>
<p>Tablas generadas con Pandas (HTML local)</p>
 
  <h2>1) Tabla original</h2>
  {tabla_original}
 
  <h2>2) Ordenada por Importe (desc)</h2>
  {tabla_ordenada}
 
  <h2>3) Filtrada: Importe >= 3000</h2>
  {tabla_filtrada}
</body>
</html>
"""
 
#6) Guardar el HTML en un archivo
with open('informe_ventas.html', 'w', encoding='utf-8') as f:
    f.write(html)  

#7) Abrir el archivo HTML en el navegador predeterminado

webbrowser.open('file://' + os.path.realpath('informe_ventas.html'))
 
