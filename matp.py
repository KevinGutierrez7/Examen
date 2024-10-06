import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Datos de ejemplo para las columnas (en este caso generados aleatoriamente para ilustración)
np.random.seed(42)

# Columna: Edad (Distribución Normal)
edad = np.random.normal(42, 10, 1000)

# Columna: Ingreso (Distribución Log-normal)
ingreso = np.random.lognormal(np.log(58805), 0.75, 1000)

# Columna: Tiempo Total Pasado (Distribución Exponencial)
tiempo_total = np.random.exponential(152, 1000)

# Columna: Número de Sesiones (Distribución Poisson)
numero_sesiones = np.random.poisson(10, 1000)

# Columna: Duración del Video (Distribución Normal)
duracion_video = np.random.normal(15, 5, 1000)

# Columna: Interacción (Distribución Log-normal)
interaccion = np.random.lognormal(np.log(5016), 0.75, 1000)

# Columna: Puntuación de Importancia (Distribución Normal)
puntuacion_importancia = np.random.normal(5, 2, 1000)

# Columna: Tiempo Pasado en Video (Distribución Exponencial)
tiempo_video = np.random.exponential(15, 1000)

# Columna: Número de Videos Vistos (Distribución Poisson)
numero_videos = np.random.poisson(25, 1000)

# Columna: Tasa de Desplazamiento (Distribución Normal)
tasa_desplazamiento = np.random.normal(50, 15, 1000)

# Columna: Pérdida de Productividad (Distribución Normal)
perdida_productividad = np.random.normal(5, 2, 1000)

# Columna: Satisfacción (Distribución Normal)
satisfaccion = np.random.normal(5, 2, 1000)

# Columna: Autocontrol (Distribución Normal)
autocontrol = np.random.normal(7, 2, 1000)

# Columna: Nivel de Adicción (Distribución Normal)
nivel_adiccion = np.random.normal(3, 1.5, 1000)

# Crear un diccionario de las columnas y los datos
columnas = {
    'Edad (Normal)': edad,
    'Ingreso (Log-normal)': ingreso,
    'Tiempo Total Pasado (Exponencial)': tiempo_total,
    'Número de Sesiones (Poisson)': numero_sesiones,
    'Duración del Video (Normal)': duracion_video,
    'Interacción (Log-normal)': interaccion,
    'Puntuación de Importancia (Normal)': puntuacion_importancia,
    'Tiempo Pasado en Video (Exponencial)': tiempo_video,
    'Número de Videos Vistos (Poisson)': numero_videos,
    'Tasa de Desplazamiento (Normal)': tasa_desplazamiento,
    'Pérdida de Productividad (Normal)': perdida_productividad,
    'Satisfacción (Normal)': satisfaccion,
    'Autocontrol (Normal)': autocontrol,
    'Nivel de Adicción (Normal)': nivel_adiccion
}

# Graficar las distribuciones
plt.figure(figsize=(16, 24))

for i, (columna, data) in enumerate(columnas.items(), 1):
    plt.subplot(5, 3, i)
    sns.histplot(data, kde=True)
    plt.title(f'{columna}')

plt.tight_layout()
plt.show()
