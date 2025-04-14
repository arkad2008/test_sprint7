import pandas as pd
import scipy.stats
import streamlit as st
import time

# Variables de estado de la sesión que se conservan al recargar
if 'experiment_no' not in st.session_state:
    st.session_state['experiment_no'] = 0

if 'df_experiment_results' not in st.session_state:
    st.session_state['df_experiment_results'] = pd.DataFrame(columns=['no', 'iteraciones', 'media'])

# Título de la aplicación
st.header('Lanzar una moneda')

# Inicializar el gráfico con un valor inicial
chart = st.line_chart([0.5])

# Función para emular el lanzamiento de monedas
def toss_coin(n):
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)  # Resultados aleatorios
    mean = None
    outcome_no = 0
    outcome_1_count = 0

    # Calcular la media acumulativa y actualizar el gráfico
    for r in trial_outcomes:
        outcome_no += 1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count / outcome_no
        chart.add_rows([mean])
        time.sleep(0.05)  # Pausa para animación

    return mean

# Widgets para configurar el experimento
number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10, key='slider_number_of_trials')
start_button = st.button('Ejecutar', key='start_button_key')

# Acción cuando se hace clic en el botón
if start_button:
    st.session_state['experiment_no'] += 1  # Incrementar número del experimento
    st.write(f'Iniciando el experimento {st.session_state["experiment_no"]} con {number_of_trials} intentos...')
    
    # Ejecutar el experimento y calcular la media
    mean = toss_coin(number_of_trials)
    st.write(f'La media final después de {number_of_trials} intentos es: {mean}')
    
    # Guardar resultados en el DataFrame de la sesión
    new_result = {
        'no': st.session_state['experiment_no'],
        'iteraciones': number_of_trials,
        'media': mean
    }
    st.session_state['df_experiment_results'] = pd.concat(
        [st.session_state['df_experiment_results'], pd.DataFrame([new_result])],
        ignore_index=True
    )
    
    # Mostrar la tabla de resultados
    st.write('Resultados de todos los experimentos:')
    st.dataframe(st.session_state['df_experiment_results'])
