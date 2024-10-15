import pdfplumber  # type: ignore
import re

# Función que procesa las líneas para extraer los datos de Naranja
def procesar_informacion_naranja(lineas):
    data = []
    for linea in lineas:
        fecha = re.search(r"Fecha de pago: (\d{2}/\d{2}/\d{4})", linea)
        nro_pago = re.search(r"Nro de pago: (\d+)", linea)
        neto = re.search(r"Neto: ([0-9,.]+)", linea)
        iva = re.search(r"IVA: ([0-9,.]+)", linea)
        percepcion_iva = re.search(r"Percepcion IVA: ([0-9,.]+)", linea)

        if fecha and nro_pago and neto and iva and percepcion_iva:
            fila = {
                'Fecha de Pago': fecha.group(1),
                'Nro de Pago': nro_pago.group(1),
                'Neto': neto.group(1),
                'IVA': iva.group(1),
                'Percepcion IVA': percepcion_iva.group(1),
            }
            data.append(fila)

    return data

# Función que procesa las líneas para extraer los datos de Amex
def procesar_informacion_amex(lineas):
    data = []
    resumen_mensual = None
    iva_debito = None
    percepcion_iva = None
    retencion_iibb = None
    total_procesadas = None

    for linea in lineas:
        # Busca el resumen mensual
        if "RESUMEN MENSUAL DE OPERACIONES NO." in linea:
            resumen_mensual = linea.strip()

        # Usa expresiones regulares para buscar los datos
        iva_debito_match = re.search(r"IVA DEBITO FISCAL\s+([0-9,.]+)", linea)
        percepcion_iva_match = re.search(r"PERCEP IVA R.G. DGI\s+\d+\s+([0-9,.]+)", linea)
        retencion_iibb_match = re.search(r"RETENCION IIBB - SIRTAC\s+([0-9,.]+)", linea)
        total_procesadas_match = re.search(r"TOTAL PROCESADAS\s+([0-9,.]+)", linea)

        if iva_debito_match:
            iva_debito = iva_debito_match.group(1).strip()
        if percepcion_iva_match:
            percepcion_iva = percepcion_iva_match.group(1).strip()
        if retencion_iibb_match:
            retencion_iibb = retencion_iibb_match.group(1).strip()
        if total_procesadas_match:
            total_procesadas = total_procesadas_match.group(1).strip()

    # Agrega la información a una fila si se encontró información
    if resumen_mensual or iva_debito or percepcion_iva or retencion_iibb or total_procesadas:
        fila = {
            'Resumen Mensual': resumen_mensual,
            'IVA Débito Fiscal': iva_debito,
            'Percepción IVA': percepcion_iva,
            'Retención IIBB': retencion_iibb,
            'Total Procesadas': total_procesadas,
        }
        data.append(fila)

    return data

# Función que extrae las líneas de texto de un PDF
def extraer_informacion_pdf(archivo_pdf, tipo_documento):
    informacion = []
    
    with pdfplumber.open(archivo_pdf) as pdf:
        for pagina in pdf.pages:
            texto = pagina.extract_text()
            if texto:
                lineas = texto.split('\n')
                
                if tipo_documento == "naranja":
                    informacion += procesar_informacion_naranja(lineas)

                elif tipo_documento == "amex":
                    informacion += procesar_informacion_amex(lineas)
    
    return informacion

# Ejemplo de uso
tipo_documento = input("Selecciona el PDF que deseas procesar:\n1. Naranja\n2. Amex\nIngresa el número de tu elección (1 o 2): ")
ruta_pdf = r"C:\Users\Monica\Desktop\Leer PDF\naranja.pdf" if tipo_documento == "1" else r"C:\Users\Monica\Desktop\Leer PDF\amex.pdf"

informacion_procesada = extraer_informacion_pdf(ruta_pdf, "naranja" if tipo_documento == "1" else "amex")

for info in informacion_procesada:
    print(info)
