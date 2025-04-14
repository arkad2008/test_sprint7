import streamlit as st

# Título de la aplicación
st.header('Lanzar una moneda')

# Mensaje inicial
st.write('Esta aplicación aún no es funcional. En construcción.')


import streamlit as st

st.header('Lanzar una moneda')

number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)
start_button = st.button('Ejecutar')

if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso.')

st.write('Esta aplicación aún no es funcional. En construcción.')


import scipy.stats
import streamlit as st
import time

# Título de la aplicación
st.header('Lanzar una moneda')

# Inicializar el gráfico de líneas
chart = st.line_chart([0.5])

# Función para emular el lanzamiento de monedas
def toss_coin(n):
    # Generar resultados de lanzamientos usando distribución Bernoulli
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)

    mean = None
    outcome_no = 0
    outcome_1_count = 0

    # Calcular la media y actualizar el gráfico
    for r in trial_outcomes:
        outcome_no += 1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count / outcome_no
        chart.add_rows([mean])  # Añadir la media al gráfico
        time.sleep(0.05)

    return mean

# Widgets de entrada para configurar el experimento
number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10, key='slider_number_of_trials')
start_button = st.button('Ejecutar', key='start_button_key')

# Acción cuando se hace clic en el botón
if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso.')
    final_mean = toss_coin(number_of_trials)  # Llamar a la función de lanzamiento
    st.write(f'La media final después de {number_of_trials} intentos es: {final_mean}')
    


import scipy.stats
import streamlit as st
import time

st.header('Lanzar una moneda')

chart = st.line_chart([0.5])

def toss_coin(n):

    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)

    mean = None
    outcome_no = 0
    outcome_1_count = 0

    for r in trial_outcomes:
        outcome_no +=1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count / outcome_no
        chart.add_rows([mean])
        time.sleep(0.05)

    return mean

number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10, key='slider_unique_key')
start_button = st.button('Ejecutar', key='start_button_key')

if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso.')
    mean = toss_coin(number_of_trials)
