import csv

def calcular_percentil(datos, percentil):
    datos_ordenados = sorted(datos)
    n = len(datos_ordenados)
    k = (n - 1) * (percentil / 100)
    f = int(k)
    c = k - f
    if f + 1 < n:
        return datos_ordenados[f] + c * (datos_ordenados[f + 1] - datos_ordenados[f])
    else:
        return datos_ordenados[f]

def calcular_cuartil(datos, cuartil):
    return calcular_percentil(datos, cuartil * 25)

# Leer el archivo CSV
ruta_csv = r'C:\Users\pc\Downloads\Time-Wasters on Social Media.csv'  # Ajusta la ruta de tu archivo CSV
columnas = {}
columnas_a_omitir = ["Género", "Ubicación", "Deuda", "Propiedad", "Profesión", 
                     "Demografía", "Plataforma", "Categoría de Video", 
                     "Frecuencia", "Razón para Ver", "Tipo de Dispositivo", 
                     "SO", "Actividad Actual", "Tipo de Conexión", "Tiempo de Visualización"]

try:
    with open(ruta_csv, mode='r', encoding='ISO-8859-1') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv, delimiter=';')  # Establecer el delimitador como punto y coma
        
        # Leer datos
        for fila in lector_csv:
            for columna, valor in fila.items():
                if columna in columnas_a_omitir:
                    continue  # Omitir columnas no deseadas
                if columna not in columnas:
                    columnas[columna] = []
                # Asegurarse de que los valores sean numéricos
                try:
                    columnas[columna].append(float(valor))
                except ValueError:
                    print(f'Valor no numérico encontrado en la columna "{columna}": {valor}')  # Depuración: muestra valores no numéricos

except FileNotFoundError:
    print(f'Error: El archivo no se encontró en la ruta: {ruta_csv}')
except Exception as e:
    print(f'Error al abrir el archivo: {e}')

# Solicitar al usuario qué percentiles desea calcular
percentiles_a_calcular = input("Introduce los percentiles que deseas calcular (separados por comas, por ejemplo: 25,50,75): ")
percentiles_a_calcular = [int(p.strip()) for p in percentiles_a_calcular.split(',')]

# Calcular percentiles y cuartiles para cada columna
for columna, datos in columnas.items():
    if datos:  # Solo proceder si hay datos numéricos en la columna
        print(f'\nColumna: {columna}')
        print(f'Datos en la columna: {datos}')
        
        for percentil in percentiles_a_calcular:
            print(f'Percentil {percentil}: {calcular_percentil(datos, percentil)}')
        
        # Calcular cuartiles
        print(f'Cuartil 1: {calcular_cuartil(datos, 1)}')
        print(f'Cuartil 2 (Mediana): {calcular_cuartil(datos, 2)}')
        print(f'Cuartil 3: {calcular_cuartil(datos, 3)}\n')
    else:
        print(f'No hay datos numéricos en la columna: {columna}')  
