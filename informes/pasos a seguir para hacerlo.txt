import pandas as pd
 
#1) Ruta del archivo CSV
ficheros_csv ='datos_ventas.csv'
 
#2)Leer el archivo CSV y cargarlo en un DataFrame de pandas
df = pd.read_csv(ficheros_csv)
 
#3) Crear una tabla para imprimir el DataFrame
tabla_estetica = df.to_html()
 
#4) Imprimir el DataFrame
print(df)

#(paso 5 filtrado de datos (eliminar columna de mes))
df_sin_mes = df.drop(columns=['Mes'])
tabla_estetica = df_sin_mes.to_html(index=False)
#(index=False) para eliminar la columna de índices en la tabla HTML

# 4) Montar un HTML completo (con título + estilo básico)
html_completo = f"""
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Informe de Ventas</title> 
<style>
    body {{
      font-family: Arial, sans-serif;
      margin: 30px;
    }}
    h1 {{
      margin-bottom: 5px;
    }}
    p {{
      color: #555;
      margin-top: 0;
    }}
    table {{
      border-collapse: collapse;
      width: 100%;
      margin-top: 15px;
    }}
    th, td {{
      border: 1px solid #ddd;
      padding: 10px;
      text-align: left;
    }}
    th {{
      background: #f2f2f2;
    }}
    tr:nth-child(even) {{
      background: #fafafa;
    }}
</style>
</head>
<body>
<h1>Grupo DAM</h1> 
<p>Generado con Pandas (sin Datapane)</p>
 
  <h2>Tabla de datos</h2>
  {tabla_estetica}
</body>
</html>
"""

#6) Guardar el HTML en un archivo
with open('informe_ventas.html', 'w', encoding='utf-8') as f:
    f.write(html_completo)  

#7) Abrir el archivo HTML en el navegador predeterminado
import webbrowser       
import os
webbrowser.open('file://' + os.path.realpath('informe_ventas.html'))
 

