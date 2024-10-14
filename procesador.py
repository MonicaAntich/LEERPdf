import re

def procesar_informacion(lineas):
    data = []

    for linea in lineas:
        fecha = re.search(r"Fecha de pago: (\d{2}/\d{2}/\d{4})", linea)
        nro_pago = re.search(r"Nro de pago: (\d+)", linea)
        neto = re.search(r"Neto: ([0-9,.]+)", linea)
        iva = re.search(r"IVA: ([0-9,.]+)", linea)
        percepcion_iva = re.search(r"Percepcion IVA: ([0-9,.]+)", linea)
        # Continúa con las demás percepciones o retenciones

        if fecha and nro_pago and neto and iva and percepcion_iva:
            fila = {
                'Fecha de Pago': fecha.group(1),
                'Nro de Pago': nro_pago.group(1),
                'Neto': neto.group(1),
                'IVA': iva.group(1),
                'Percepcion IVA': percepcion_iva.group(1),
                # Añadir los demás campos
            }
            data.append(fila)
    
    return data
