import scipy.stats
import streamlit as st
import time

# Título de la aplicación (solo una vez)
st.title('Lanzar una moneda')

# Inicializar el gráfico de líneas con un valor inicial
chart = st.line_chart([0.5])

# Función para emular el lanzamiento de monedas
def toss_coin(n):
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)  # Generar lanzamientos
    mean = None
    outcome_no = 0
    outcome_1_count = 0

    # Calcular la media acumulativa y actualizar el gráfico
    for r in trial_outcomes:
        outcome_no += 1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count / outcome_no
        chart.add_rows([mean])  # Añadir la media al gráfico
        time.sleep(0.05)  # Breve pausa para visualización

    return mean

# Widget: control deslizante para número de intentos
number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10, key='slider_number_of_trials')

# Widget: botón para iniciar el experimento
start_button = st.button('Ejecutar', key='start_button_key')

# Acción cuando se hace clic en el botón
if start_button:
    st.write(f'Iniciando el experimento con {number_of_trials} intentos...')
    final_mean = toss_coin(number_of_trials)  # Llamar a la función de lanzamiento
    st.write(f'La media final después de {number_of_trials} intentos es: {final_mean}')
