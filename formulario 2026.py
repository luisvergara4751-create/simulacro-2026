nombre = st.text_input("Ingresa tu nombre completo:")

# Opciones de candidatos
candidato = st.radio(
    "Selecciona tu candidato preferido:",
    ["Rafael López Aliaga", "César Acuña", "Voto en Blanco"]
)

# Botón de acción
if st.button("Registrar mi Voto"):
    if nombre:
        st.success(f"¡Excelente {nombre}! Tu voto por {candidato} ha sido registrado con éxito.")
        st.balloons() # Esto tira globos de celebración en la pantalla
    else:
        st.error("Por favor, ingresa tu nombre antes de votar.")
