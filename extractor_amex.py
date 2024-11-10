# import pdfplumber
# import re  # Usaremos expresiones regulares para extraer los datos

# def extraer_amex_pdf(archivo_pdf, tipo_documento):
#     print("Entré a la búsqueda del amex")
#     # Diccionario para almacenar los últimos valores encontrados
#     pago_info = {
#         "Resumen mensual de operaciones": None,
#         "Fecha de Emisión": None
#     }
    
#     # Definir las expresiones regulares para buscar los valores
#     regex_resumen = r"RESUMEN MENSUAL DE OPERACIONES NO\. (\d+-\d+)"
#     regex_fecha_emision = r"FECHA DE EMISION: (\d{2}/\d{2}/\d{4})"

#     with pdfplumber.open(archivo_pdf) as pdf:
#         for pagina in pdf.pages:
#             texto = pagina.extract_text()
#             if texto:
#                 lineas = texto.split('\n')
                
#                 if tipo_documento == "amex":
#                     for linea in lineas:
#                         # Buscar "Resumen mensual de operaciones"
#                         match_resumen = re.search(regex_resumen, linea)
#                         if match_resumen:
#                             pago_info["Resumen mensual de operaciones"] = match_resumen.group(1)
    
#                         # Buscar "Fecha de emisión"
#                         match_fecha = re.search(regex_fecha_emision, linea)
#                         if match_fecha:
#                             pago_info["Fecha de Emisión"] = match_fecha.group(1)

#     return pago_info

import pdfplumber
import re  # Usaremos expresiones regulares para extraer los datos

def extraer_amex_pdf(archivo_pdf, tipo_documento):
    print("Entré a la búsqueda del amex")
    # Diccionario para almacenar los últimos valores encontrados
    pago_info = {
        "Resumen mensual de operaciones": None,
        "Fecha de Emisión": None
    }
    
    # Definir las expresiones regulares para buscar los valores
    regex_resumen = r"RESUMEN MENSUAL DE OPERACIONES NO\. (\d+-\d+)"
    regex_fecha_emision = r"FECHA DE EMISION: (\d{2}/\d{2}/\d{4})"

    with pdfplumber.open(archivo_pdf) as pdf:
        for pagina in pdf.pages:
            texto = pagina.extract_text()
            if texto:
                lineas = texto.split('\n')
                
                if tipo_documento == "amex":
                    for linea in lineas:
                        # Buscar "Resumen mensual de operaciones"
                        match_resumen = re.search(regex_resumen, linea)
                        if match_resumen:
                            pago_info["Resumen mensual de operaciones"] = match_resumen.group(1)
    
                        # Buscar "Fecha de emisión"
                        match_fecha = re.search(regex_fecha_emision, linea)
                        if match_fecha:
                            pago_info["Fecha de Emisión"] = match_fecha.group(1)

    return pago_info
