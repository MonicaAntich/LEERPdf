import pdfplumber # type: ignore

def extraer_informacion_pdf(naranja_pdf):
    informacion = []
    tipo_y_numero_recuperado = False  # Para capturar "Tipo y Nº" solo una vez
    fecha_emision_recuperada = False  # Para capturar la "Fecha de Emisión" solo una vez
    sirtac_recuperado = False  # Para capturar el importe de "Sirtac" solo una vez

    with pdfplumber.open(naranja_pdf) as pdf:
        for pagina in pdf.pages:
            texto = pagina.extract_text()
            if texto:
                lineas = texto.split('\n')
                pago_info = {}

                for linea in lineas:
                    # Captura "Tipo y Nº" solo una vez, sin incluir "Hoja Nº"
                    if "Tipo y Nº:" in linea and not tipo_y_numero_recuperado:
                        pago_info["Tipo y Nº"] = linea.split("Tipo y Nº:")[-1].strip().split("Hoja")[0].strip()
                        tipo_y_numero_recuperado = True  # Solo se captura una vez

                    # Captura "Fecha de Emisión" solo una vez
                    elif "Fecha de Emisión:" in linea and not fecha_emision_recuperada:
                        pago_info["Fecha de Emisión"] = linea.split("Fecha de Emisión:")[-1].strip()
                        fecha_emision_recuperada = True  # Solo se captura una vez

                    # Captura el importe de "Sirtac"
                    elif "Sirtac" in linea and not sirtac_recuperado:
                        partes = linea.split()  # Dividir la línea por espacios
                        pago_info["Sirtac"] = partes[-1]  # El último elemento es el importe
                        sirtac_recuperado = True  # Solo se captura una vez

                    # Captura los detalles de facturación
                    elif "Arancel" in linea:
                        pago_info["Arancel"] = linea.split()[-1].strip()  # Suponiendo que el importe está al final
                    elif "Transferencia Electrónica" in linea:
                        pago_info["Transferencia Electrónica"] = linea.split()[-1].strip()
                    elif "Percepción de IVA 3.0 %" in linea:
                        pago_info["Percepción de IVA 3.0 %"] = linea.split()[-1].strip()
                    elif "IVA 21.0 %" in linea:
                        pago_info["IVA 21.0 %"] = linea.split()[-1].strip()

                if pago_info:  # Asegúrate de agregar solo si hay información en la página
                    informacion.append(pago_info)

    return informacion
