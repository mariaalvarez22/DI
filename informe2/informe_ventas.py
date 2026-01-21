import pandas as pd
import matplotlib.pyplot as plt
import webbrowser
import os
from pathlib import Path


# TAREA 1 
df = pd.read_csv('datos_ventas.csv')

print(df.head())
print(df.columns)

# TAREA 2 
Path("salida").mkdir(exist_ok=True)
df.to_html("salida/tabla_datos.html", index=False)


#CREA TAREA 3 
total_unidades = df["Unidades"].sum()
total_importe = df["Importe"].sum()
media_unidades = df["Unidades"].mean()

top_comercial = df.groupby("Nombre")["Importe"].sum().sort_values(ascending=False).head(1)

print("Total unidades:", total_unidades)
print("Total importe:", total_importe)
print("Media unidades:", media_unidades)
print("Comercial con mayor importe:")
print(top_comercial)


# TAREA 4 — Gráficos
# 1) Gráfico de líneas
unidades_mes = df.groupby("Mes")["Unidades"].sum()
plt.figure()
unidades_mes.plot(kind="line", marker="o")
plt.title("Evolución de unidades vendidas por mes")
plt.xlabel("Mes")
plt.ylabel("Unidades")
plt.grid(True)
plt.savefig("grafico_lineas_unidades.png")
plt.close()

# 2) Gráfico de barras 
importe_comercial = df.groupby("Nombre")["Importe"].sum().sort_values(ascending=False)
plt.figure()
importe_comercial.plot(kind="bar")
plt.title("Importe total por comercial")
plt.xlabel("Comercial")
plt.ylabel("Importe (€)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("grafico_barras_importe.png")
plt.close()

# 3) Gráfico sector 
unidades_comercial = df.groupby("Nombre")["Unidades"].sum()
plt.figure()
unidades_comercial.plot(kind="pie", autopct="%1.1f%%", startangle=90)
plt.title("Reparto de unidades por comercial")
plt.ylabel("")
plt.tight_layout()
plt.savefig("grafico_sector_unidades.png")
plt.close()

# TAREA 5 — Informe final HTML
html = f"""
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Informe de Ventas</title>
<style>
    body {{ font-family: Arial; margin: 30px; background:#f7f7f7; }}
    h1 {{ text-align:center; }}
    .texto {{ max-width: 900px; margin:auto; }}
    .grafico {{ text-align:center; margin:30px 0; }}
    img {{ max-width:100%; border:1px solid #ccc; background:#fff; padding:10px; }}
</style>
</head>
<body>
<h1>Informe de Ventas Anual</h1>
<div class="texto">
<p>Este informe muestra la evolución de ventas durante el año</p>
</div>

<div class="grafico">
<h2>1) Evolución unidades por mes</h2>
<img src="../grafico_lineas_unidades.png" alt="Gráfico líneas">
</div>

<div class="grafico">
<h2>2) Importe total por comercial</h2>
<img src="../grafico_barras_importe.png" alt="Gráfico barras">
</div>

<div class="grafico">
<h2>3) Reparto de unidades por comercial</h2>
<img src="../grafico_sector_unidades.png" alt="Gráfico sector">
</div>

</body>
</html>
"""

with open("salida/informe_final.html", "w", encoding="utf-8") as f:
    f.write(html)

webbrowser.open('file://' + os.path.realpath('salida/informe_final.html'))
