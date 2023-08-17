import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta as beta_dist

def generar_grafico_pert(durOpt, durProb, durPes):
    # Función para calcular la duración esperada según el método PERT
    def calculate_pert_estimate(durOpt, durProb, durPes):
        return (durOpt + 4 * durProb + durPes) / 6

    # Calcular la duración esperada usando el método PERT
    esperada = calculate_pert_estimate(durOpt, durProb, durPes)
    varianza = ((durPes - durOpt) / 6) ** 2
    desvEstandar = np.sqrt(varianza)

    # Calcular los parámetros 'alpha' y 'beta' para la distribución Beta
    alpha = 1 + (4 * durProb - durOpt - durPes) / 6
    beta = 1 + (durPes - durOpt) / 6

    # Crear una distribución Beta con los parámetros calculados
    dist = beta_dist(alpha, beta)

    # Generar valores de tiempo para graficar la distribución (en días)
    x = np.linspace(durOpt, durPes, 1000)

    # Calcular los valores de probabilidad correspondientes a los días
    y = dist.pdf((x - durOpt) / (durPes - durOpt))

    # Graficar la distribución Beta y la línea de la duración esperada
    plt.plot(x, y, label='Distribución Beta')  # Gráfica de la distribución Beta
    plt.axvline(esperada, color='red', linestyle='dashed', label='Duración Esperada')  # Línea para la duración esperada
    plt.xlabel('Duración (días)')  # Etiqueta del eje X
    plt.ylabel('Probabilidad')  # Etiqueta del eje Y
    plt.title('Distribución Beta para la Actividad')  # Título de la gráfica
    plt.legend()  # Mostrar leyenda
    plt.grid(True)  # Habilitar cuadrícula en la gráfica

    # Exportar el gráfico como una imagen PNG
    plt.savefig('..\\simulador\\img\\grafico_pert.jpeg', dpi=300)

    # Mostrar la gráfica en una ventana (opcional)
    # plt.show()
    return (esperada,varianza,desvEstandar)
