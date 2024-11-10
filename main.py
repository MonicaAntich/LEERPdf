# import pandas as pd  
# from extractor_naranja import extraer_naranja_pdf
# from extractor_amex import extraer_amex_pdf

# def guardar_en_excel(data, archivo_excel):
#     df = pd.DataFrame(data)
#     df.to_excel(archivo_excel, index=False)

# # Función principal para ejecutar el programa

# def main():
#     # Solicitar al usuario que elija qué PDF procesar
#     print("Selecciona el PDF que deseas procesar:")
#     print("1. Naranja")
#     print("2. Amex")
    
#     # Obtener la opción del usuario
#     opcion = input("Ingresa el número de tu elección (1 o 2): ")

#     # Definir las rutas y las funciones según la elección
#     if opcion == '1':
#         ruta_pdf = r"C:\leer_pdf\naranja.pdf"
#         archivo_excel = "informacion_pago_naranja.xlsx"
#         tipo_documento = "naranja"  # Tipo de documento para Naranja

#         # Llamar al método de Naranja
#         informacion_pdf = extraer_naranja_pdf(ruta_pdf, tipo_documento)
    
#     elif opcion == '2':
#         ruta_pdf = r"C:\leer_pdf\amex.pdf"
#         archivo_excel = "informacion_pago_amex.xlsx"
#         tipo_documento = "amex"  # Tipo de documento para Amex

#         # Llamar al método de Amex
#         informacion_pdf = extraer_amex_pdf(ruta_pdf, tipo_documento)
    
#     else:
#         print("Opción no válida. Por favor, elige 1 o 2.")
#         return  # Terminar el programa si la opción no es válida




#     print(f"\nInformación {tipo_documento.capitalize()}:")
#     for clave, valor in informacion_pdf.items():
#         print(f"{clave}: {valor}")  # Imprime cada par clave-valor


#     # # Publicar la información adquirida por consola
#     # print(f"\nInformación {tipo_documento.capitalize()}:")
#     # for pago_info in informacion_pdf:
#     #     for clave, valor in pago_info.items():
#     #         print(f"{clave}: {valor}")  # Imprime cada par clave-valor

#     # Guardar la información extraída en un archivo Excel
#     #guardar_en_excel(informacion_pdf, archivo_excel)
#     #print(f"Información guardada en {archivo_excel}")

# if __name__ == "__main__":
#     main()
import pandas as pd  
from extractor_naranja import extraer_naranja_pdf
from extractor_amex import extraer_amex_pdf

def guardar_en_excel(data, archivo_excel):
    df = pd.DataFrame([data])  # Convertir a DataFrame un solo diccionario
    df.to_excel(archivo_excel, index=False)

# Función principal para ejecutar el programa
def main():
    # Solicitar al usuario que elija qué PDF procesar
    print("Selecciona el PDF que deseas procesar:")
    print("1. Naranja")
    print("2. Amex")
    
    # Obtener la opción del usuario
    opcion = input("Ingresa el número de tu elección (1 o 2): ")

    # Definir las rutas y las funciones según la elección
    if opcion == '1':
        ruta_pdf = r"C:\leer_pdf\naranja.pdf"
        archivo_excel = "informacion_pago_naranja.xlsx"
        tipo_documento = "naranja"  # Tipo de documento para Naranja

        # Llamar al método de Naranja
        informacion_pdf = extraer_naranja_pdf(ruta_pdf, tipo_documento)
    
    elif opcion == '2':
        ruta_pdf = r"C:\leer_pdf\amex.pdf"
        archivo_excel = "informacion_pago_amex.xlsx"
        tipo_documento = "amex"  # Tipo de documento para Amex

        # Llamar al método de Amex
        informacion_pdf = extraer_amex_pdf(ruta_pdf, tipo_documento)
    
    else:
        print("Opción no válida. Por favor, elige 1 o 2.")
        return  # Terminar el programa si la opción no es válida

    print(f"\nInformación {tipo_documento.capitalize()}:")
    for clave, valor in informacion_pdf.items():
        print(f"{clave}: {valor}")  # Imprime cada par clave-valor

    # # Guardar la información extraída en un archivo Excel
    # guardar_en_excel(informacion_pdf, archivo_excel)
    # print(f"Información guardada en {archivo_excel}")

if __name__ == "__main__":
    main()
