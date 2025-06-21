import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Leer personas y montos desde archivo txt
def leer_datos_txt(path):
    personas = []
    try:
        with open(path, 'r') as f:
            for linea in f:
                if ',' in linea:
                    nombre, monto = linea.strip().split(',')
                    personas.append((nombre.strip(), float(monto.strip())))
    except Exception as e:
        print("Error leyendo archivo:", e)
    return personas

# Analizar los datos
def analizar_datos(personas):
    if not personas:
        return None
    mas_plata = max(personas, key=lambda x: x[1])
    menos_plata = min(personas, key=lambda x: x[1])
    promedio = sum(p[1] for p in personas) / len(personas)
    return {
        'más_rico': mas_plata,
        'más_pobre': menos_plata,
        'promedio': promedio
    }

# Conexión a Google Sheets
def connect_sheet():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open("Bitcoin Prices").sheet1  # Cambiá el nombre si tu hoja tiene otro
    return sheet

# Escribir tabla y análisis en la hoja (col A y B)
def escribir_personas_y_analisis(sheet, personas, analisis):
    start_row = 1
    start_col = 1  # Columna A

    # Encabezado
    sheet.update_cell(start_row, start_col, 'Nombre')
    sheet.update_cell(start_row, start_col + 1, 'Dinero')

    # Datos
    for i, (nombre, monto) in enumerate(personas):
        sheet.update_cell(start_row + i + 1, start_col, nombre)
        sheet.update_cell(start_row + i + 1, start_col + 1, monto)

    # Análisis
    offset = len(personas) + 2
    sheet.update_cell(start_row + offset, start_col, 'Más rico')
    sheet.update_cell(start_row + offset, start_col + 1, f'{analisis["más_rico"][0]} (${analisis["más_rico"][1]})')

    sheet.update_cell(start_row + offset + 1, start_col, 'Más pobre')
    sheet.update_cell(start_row + offset + 1, start_col + 1, f'{analisis["más_pobre"][0]} (${analisis["más_pobre"][1]})')

    sheet.update_cell(start_row + offset + 2, start_col, 'Promedio')
    sheet.update_cell(start_row + offset + 2, start_col + 1, f'${analisis["promedio"]:.2f}')

# Programa principal
def main():
    personas = leer_datos_txt('datos.txt')
    if not personas:
        print("No hay datos válidos.")
        return

    analisis = analizar_datos(personas)
    sheet = connect_sheet()
    escribir_personas_y_analisis(sheet, personas, analisis)
    print("Datos y análisis escritos en columnas A y B de Google Sheets.")

if __name__ == "__main__":
    main()
