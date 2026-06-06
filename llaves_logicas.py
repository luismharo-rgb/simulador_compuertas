import streamlit as st

# --- CONFIGURACIÓN DE LA PÁGINA WEB ---
st.set_page_config(page_title="Simulador de Puertas Lógicas", page_icon="🎛️", layout="wide")

# Estilos personalizados para emular el color azul profesional de tu app original
st.markdown("""
    <style>
    .main { background-color: #1c8ada; }
    h1, h2, h3, p, label { color: white !important; }
    div[data-testid="stMarkdownContainer"] pre { background-color: #0f4c75 !important; color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# 1. Título principal
st.title("SIMULADOR DE PUERTAS LÓGICAS - GRUPO 5")
st.write("Interactúa con los interruptores para ver el comportamiento de las compuertas y sus tablas de verdad en tiempo real.")
st.write("---")

# Funciones auxiliares de lógica matemática que creaste
def to_vf(val): 
    return "V" if val else "F"

def evaluate_logic(x, y, g):
    if g == 'AND': return x and y
    if g == 'OR': return x or y
    if g == 'NAND': return not (x and y)
    if g == 'NOR': return not (x or y)
    if g == 'NOT': return not x

def gen_table_text(curr_a, curr_b, gate):
    lines = []
    if gate != 'NOT':
        lines.append(" A   B | Y ")
        lines.append("-" * 11)
        for i in [True, False]:
            for j in [True, False]:
                res = evaluate_logic(i, j, gate)
                prefix = "►" if (i == curr_a and j == curr_b) else " "
                lines.append(f"{prefix}{to_vf(i)}   {to_vf(j)} | {to_vf(res)}")
    else:
        lines.append(" A | Y ")
        lines.append("-" * 7)
        for i in [True, False]:
            res = evaluate_logic(i, None, gate)
            prefix = "►" if (i == curr_a) else " "
            lines.append(f"{prefix}{to_vf(i)} | {to_vf(res)}")
    return "\n".join(lines)

# Lista de compuertas
gates = ['AND', 'OR', 'NOT', 'NAND', 'NOR']

# Creación de filas interactivas (Streamlit las acomoda perfectamente en grilla web)
for gate in gates:
    # Creamos 5 columnas para distribuir el espacio como en tu interfaz original
    col1, col2, col3, col4, col5 = st.columns([1.5, 1, 1, 1.5, 2])
    
    with col1:
        st.subheader(f"🚪 Puerta {gate}")
        
    with col2:
        # Reemplazo de tu ToggleSwitch por el de Streamlit
        sw_a = st.toggle(f"Llave A", key=f"a_{gate}")
        
    with col3:
        if gate == 'NOT':
            st.write("—")
            sw_b = False
        else:
            sw_b = st.toggle(f"Llave B", key=f"b_{gate}")
            
    # Evaluación lógica pura basada en tu algoritmo
    out = evaluate_logic(sw_a, sw_b, gate)
    
    with col4:
        # Lámpara con resplandor visual usando alertas nativas de Streamlit
        if out:
            st.success(f"💡 LÁMPARA (Y): {to_vf(out)} (ENCENDIDA)")
        else:
            st.error(f"⚫ LÁMPARA (Y): {to_vf(out)} (APAGADA)")
            
    with col5:
        # Tabla de verdad dinámica con indicador de fila activa
        tabla_texto = gen_table_text(sw_a, sw_b, gate)
        st.code(tabla_texto, language="text")
        
    st.write("---")

# Nota al pie sobre IA (Se mantiene al final de la página)