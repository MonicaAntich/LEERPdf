import pandas as pd  # type: ignore
from extractor import extraer_informacion_pdf
from extractor_amex import extraer_amex_pdf

def guardar_en_excel(data, archivo_excel):
    df = pd.DataFrame(data)
    df.to_excel(archivo_excel, index=False)

# Función principal para ejecutar el programa
def main():
    # Solicitar al usuario que elija qué PDF procesar
    print("Selecciona el PDF que deseas procesar:")
    print("1. Naranja")
    print("2. Amex")
    
    # Obtener la opción del usuario
    opcion = input("Ingresa el número de tu elección (1 o 2): ")

    # Definir las rutas según la elección
    if opcion == '1':
        ruta_pdf = r"C:\Users\Monica\Desktop\LEERPdf\naranja1607.pdf"
        archivo_excel = "informacion_pago_naranja.xlsx"
        tipo_documento = "naranja"  # Tipo de documento para Naranja
    elif opcion == '2':
        ruta_pdf = r"C:\Users\Monica\Desktop\LEERPdf\amex.pdf"
        archivo_excel = "informacion_pago_amex.xlsx"
        tipo_documento = "amex"  # Tipo de documento para Amex
    else:
        print("Opción no válida. Por favor, elige 1 o 2.")
        return  # Terminar el programa si la opción no es válida

    # Extraer la información del PDF
    informacion_pdf = extraer_informacion_pdf(ruta_pdf, tipo_documento)

    # Publicar la información adquirida por consola
    print(f"\nInformación {tipo_documento.capitalize()}:")
    for pago_info in informacion_pdf:
        for clave, valor in pago_info.items():
            print(f"{clave}: {valor}")  # Imprime cada par clave-valor

    # Guardar la información extraída en un archivo Excel
    guardar_en_excel(informacion_pdf, archivo_excel)
    print(f"Información guardada en {archivo_excel}")

if __name__ == "__main__":
    main()
