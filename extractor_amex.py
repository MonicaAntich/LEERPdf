import pdfplumber  # type: ignore

def extraer_amex_pdf(archivo_pdf, tipo_documento):
    print("entre a la busqueda del amex")
    informacion = []
    tipo_y_numero_recuperado = False  # Para capturar "Tipo y Nº" solo una vez (para el PDF de naranja)
    fecha_emision_recuperada = False  # Para capturar la "Fecha de Emisión" solo una vez (para el PDF de naranja)
    sirtac_recuperado = False  # Para capturar el importe de "Sirtac" solo una vez (para el PDF de naranja)

    with pdfplumber.open(archivo_pdf) as pdf:
        for pagina in pdf.pages:
            texto = pagina.extract_text()
            if texto:
                lineas = texto.split('\n')
                pago_info = {}

                # Condiciones para el PDF "naranja"
                if tipo_documento == "naranja":
                    for linea in lineas:
                        # Captura "Tipo y Nº" solo una vez
                        if "Tipo y Nº:" in linea and not tipo_y_numero_recuperado:
                            pago_info["Tipo y Nº"] = linea.split("Tipo y Nº:")[-1].strip().split("Hoja")[0].strip()
                            tipo_y_numero_recuperado = True

                        # Captura "Fecha de Emisión" solo una vez
                        elif "Fecha de Emisión:" in linea and not fecha_emision_recuperada:
                            pago_info["Fecha de Emisión"] = linea.split("Fecha de Emisión:")[-1].strip()
                            fecha_emision_recuperada = True

                        # Captura el importe de "Sirtac"
                        elif "Sirtac" in linea and not sirtac_recuperado:
                            partes = linea.split()  # Dividir la línea por espacios
                            pago_info["Sirtac"] = partes[-1]  # El último elemento es el importe
                            sirtac_recuperado = True

                        # Captura los detalles de facturación
                        elif "Arancel" in linea:
                            pago_info["Arancel"] = linea.split()[-1].strip()
                        elif "Transferencia Electrónica" in linea:
                            pago_info["Transferencia Electrónica"] = linea.split()[-1].strip()
                        elif "Percepción de IVA 3.0 %" in linea:
                            pago_info["Percepción de IVA 3.0 %"] = linea.split()[-1].strip()
                        elif "IVA 21.0 %" in linea:
                            pago_info["IVA 21.0 %"] = linea.split()[-1].strip()

                # Condiciones para el PDF "Amex"
                elif tipo_documento == "amex":
                    for linea in lineas:
                        # Busca y captura la información relevante de las líneas
                        if "Resumen mensual de operación" in linea:
                            pago_info["Resumen mensual de operación"] = linea.split()[-1].strip()
                        elif "IVA débito fiscal" in linea:
                            pago_info["IVA débito fiscal"] = linea.split()[-1].strip()
                        elif "Percep IVA" in linea:
                            pago_info["Percep IVA"] = linea.split()[-1].strip()
                        elif "Retención IIBB" in linea:
                            pago_info["Retención IIBB"] = linea.split()[-1].strip()
                        elif "Total procesadas" in linea:
                            pago_info["Total procesadas"] = linea.split()[-1].strip()

                if pago_info:  # Solo agregar si hay información en la página
                    informacion.append(pago_info)

    return informacion
