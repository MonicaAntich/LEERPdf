import pandas as pd # type: ignore
from extractor import extraer_informacion_pdf
from procesador import procesar_informacion  # Si decides mantener esta función

def guardar_en_excel(data, archivo_excel):
    df = pd.DataFrame(data)
    df.to_excel(archivo_excel, index=False)

# Ruta del PDF y el archivo Excel de salida
ruta_pdf = r"C:\Users\Monica\Desktop\Leer PDF\naranja.pdf"
archivo_excel = "informacion_pago.xlsx"

# Extraer la información del PDF
informacion_pdf = extraer_informacion_pdf(ruta_pdf)

# Publicar la información adquirida por consola
for pago_info in informacion_pdf:
    print("Información de pago:")
    for clave, valor in pago_info.items():
        print(f"{clave}: {valor}")  # Imprime cada par clave-valor

# Si decides procesar la información extraída
# informacion_procesada = procesar_informacion(informacion_pdf) 

# Guardar la información extraída en un archivo Excel
#guardar_en_excel(informacion_pdf, archivo_excel)
#print(f"Información guardada en {archivo_excel}")
