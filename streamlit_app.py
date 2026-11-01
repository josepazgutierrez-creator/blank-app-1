import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Consulta de Notas - INCIB",
    page_icon="🎓",
    layout="centered"
)

# Base de datos de los 25 estudiantes (Módulos 3.3 y 3.8 - 3TD 2026)
ESTUDIANTES = {
    "6051092": {
        "num": 1,
        "nie": "6051092",
        "nombre": "AMAYA OCHOA, MARTHA ESTEFANY",
        "pin": "6869",
        "m33": {'prep': 2.4, 'ejec': 5.0, 'val': 1.369, 'prelim': 8.519, 'final': 8.52, 'nivel': 4},
        "m38": {'prep': 2.5, 'ejec': 4.0, 'val': 2.3, 'prelim': 9.05, 'final': 9.05, 'nivel': 5}
    },
    "6263641": {
        "num": 2,
        "nie": "6263641",
        "nombre": "ANDRADE ALVAREZ, DEYSI MARLUVE",
        "pin": "7888",
        "m33": {'prep': 2.25, 'ejec': 5.0, 'val': 1.388, 'prelim': 8.388, 'final': 8.39, 'nivel': 4},
        "m38": {'prep': 2.5, 'ejec': 4.0, 'val': 2.2, 'prelim': 8.95, 'final': 8.95, 'nivel': 4}
    },
    "4768950": {
        "num": 3,
        "nie": "4768950",
        "nombre": "ARGUETA BELTRÁN, CLEOFÁS MELQUISEDEC",
        "pin": "4467",
        "m33": {'prep': 2.05, 'ejec': 5.0, 'val': 0.75, 'prelim': 7.55, 'final': 7.55, 'nivel': 4},
        "m38": {'prep': 2.38, 'ejec': 4.0, 'val': 2.1, 'prelim': 8.475, 'final': 8.48, 'nivel': 4}
    },
    "4301142": {
        "num": 4,
        "nie": "4301142",
        "nombre": "ARGUETA SOSA, ANDERSON ORLANDO",
        "pin": "1419",
        "m33": {'prep': 2.3, 'ejec': 5.0, 'val': 1.425, 'prelim': 8.725, 'final': 8.73, 'nivel': 4},
        "m38": {'prep': 2.38, 'ejec': 5.0, 'val': 2.3, 'prelim': 9.675, 'final': 9.68, 'nivel': 5}
    },
    "10537501": {
        "num": 5,
        "nie": "10537501",
        "nombre": "BENITEZ HERNANDEZ, YILVER AUDALY",
        "pin": "8548",
        "m33": {'prep': 1.9, 'ejec': 4.0, 'val': 1.088, 'prelim': 7.238, 'final': 7.24, 'nivel': 4},
        "m38": {'prep': 2.19, 'ejec': 4.0, 'val': 2.05, 'prelim': 8.488, 'final': 8.49, 'nivel': 4}
    },
    "6051093": {
        "num": 6,
        "nie": "6051093",
        "nombre": "CHICAS FUNES, ANDREA BEATRIZ",
        "pin": "6900",
        "m33": {'prep': 2.3, 'ejec': 5.0, 'val': 1.294, 'prelim': 8.594, 'final': 8.59, 'nivel': 4},
        "m38": {'prep': 2.5, 'ejec': 5.0, 'val': 2.3, 'prelim': 9.55, 'final': 9.55, 'nivel': 5}
    },
    "5718494": {
        "num": 7,
        "nie": "5718494",
        "nombre": "CHICAS MARTINEZ, DANIELA MERCEDES",
        "pin": "1331",
        "m33": {'prep': 2.25, 'ejec': 5.0, 'val': 1.388, 'prelim': 8.388, 'final': 8.39, 'nivel': 4},
        "m38": {'prep': 2.5, 'ejec': 5.0, 'val': 2.3, 'prelim': 9.8, 'final': 9.8, 'nivel': 5}
    },
    "6537098": {
        "num": 8,
        "nie": "6537098",
        "nombre": "DÍAZ GUEVARA, RICHARD JOSUÉ",
        "pin": "7055",
        "m33": {'prep': 2.1, 'ejec': 4.0, 'val': 0.75, 'prelim': 7.1, 'final': 7.1, 'nivel': 4},
        "m38": {'prep': 2.38, 'ejec': 4.0, 'val': 2.1, 'prelim': 8.725, 'final': 8.73, 'nivel': 4}
    },
    "6051307": {
        "num": 9,
        "nie": "6051307",
        "nombre": "GUEVARA HERNANDEZ, ANA ESTEFANY",
        "pin": "4534",
        "m33": {'prep': 2.05, 'ejec': 4.0, 'val': 1.088, 'prelim': 7.138, 'final': 7.14, 'nivel': 4},
        "m38": {'prep': 2.5, 'ejec': 5.0, 'val': 2.15, 'prelim': 9.4, 'final': 9.4, 'nivel': 5}
    },
    "6263588": {
        "num": 10,
        "nie": "6263588",
        "nombre": "HERNANDEZ BONILLA, KEYRIS LOURDES",
        "pin": "6245",
        "m33": {'prep': 2.25, 'ejec': 5.0, 'val': 1.388, 'prelim': 8.138, 'final': 8.14, 'nivel': 4},
        "m38": {'prep': 2.5, 'ejec': 5.0, 'val': 2.25, 'prelim': 9.5, 'final': 9.5, 'nivel': 5}
    },
    "6263767": {
        "num": 11,
        "nie": "6263767",
        "nombre": "HERNÁNDEZ PORTILLO, JOSÉ RENÉ",
        "pin": "2794",
        "m33": {'prep': 2.1, 'ejec': 5.0, 'val': 0.938, 'prelim': 7.538, 'final': 7.54, 'nivel': 4},
        "m38": {'prep': 2.06, 'ejec': 4.0, 'val': 2.2, 'prelim': 8.513, 'final': 8.51, 'nivel': 4}
    },
    "3562133": {
        "num": 12,
        "nie": "3562133",
        "nombre": "HERNÁNDEZ SANTOS, MARLON MILTON",
        "pin": "6140",
        "m33": {'prep': 2.3, 'ejec': 5.0, 'val': 1.388, 'prelim': 8.688, 'final': 8.69, 'nivel': 4},
        "m38": {'prep': 2.5, 'ejec': 5.0, 'val': 2.3, 'prelim': 9.55, 'final': 9.55, 'nivel': 5}
    },
    "4768982": {
        "num": 13,
        "nie": "4768982",
        "nombre": "MARAVILLA HERNÁNDEZ, ERIKA",
        "pin": "5459",
        "m33": {'prep': 2.4, 'ejec': 5.0, 'val': 1.425, 'prelim': 8.825, 'final': 8.83, 'nivel': 4},
        "m38": {'prep': 2.5, 'ejec': 5.0, 'val': 2.4, 'prelim': 9.65, 'final': 9.65, 'nivel': 5}
    },
    "6051327": {
        "num": 14,
        "nie": "6051327",
        "nombre": "MARTINEZ CRUZ, JOSSELINE JOHANA",
        "pin": "5154",
        "m33": {'prep': 2.0, 'ejec': 4.0, 'val': 1.35, 'prelim': 7.35, 'final': 7.35, 'nivel': 4},
        "m38": {'prep': 2.5, 'ejec': 5.0, 'val': 2.25, 'prelim': 9.5, 'final': 9.5, 'nivel': 5}
    },
    "6263617": {
        "num": 15,
        "nie": "6263617",
        "nombre": "MENDOZA AMAYA, DANIELA LILIBETH",
        "pin": "7144",
        "m33": {'prep': 2.35, 'ejec': 5.0, 'val': 1.5, 'prelim': 8.85, 'final': 8.85, 'nivel': 4},
        "m38": {'prep': 2.5, 'ejec': 5.0, 'val': 2.4, 'prelim': 9.9, 'final': 9.9, 'nivel': 5}
    },
    "19942461": {
        "num": 16,
        "nie": "19942461",
        "nombre": "ORELLANA ORELLANA, LINCY DAYANA",
        "pin": "7308",
        "m33": {'prep': 2.3, 'ejec': 5.0, 'val': 1.238, 'prelim': 8.038, 'final': 8.04, 'nivel': 4},
        "m38": {'prep': 2.5, 'ejec': 5.0, 'val': 2.25, 'prelim': 9.25, 'final': 9.25, 'nivel': 5}
    },
    "5717914": {
        "num": 17,
        "nie": "5717914",
        "nombre": "PORTILLO NOLASCO, CRISTIAN JAVIER",
        "pin": "1351",
        "m33": {'prep': 1.9, 'ejec': 5.0, 'val': 1.219, 'prelim': 7.619, 'final': 7.62, 'nivel': 4},
        "m38": {'prep': 2.06, 'ejec': 4.0, 'val': 2.2, 'prelim': 8.263, 'final': 8.26, 'nivel': 4}
    },
    "6051125": {
        "num": 18,
        "nie": "6051125",
        "nombre": "PORTILLO VILLALTA, ANDREA CAROLINA",
        "pin": "7892",
        "m33": {'prep': 2.35, 'ejec': 5.0, 'val': 1.294, 'prelim': 8.144, 'final': 8.14, 'nivel': 4},
        "m38": {'prep': 2.5, 'ejec': 5.0, 'val': 2.2, 'prelim': 9.2, 'final': 9.2, 'nivel': 5}
    },
    "2521317": {
        "num": 19,
        "nie": "2521317",
        "nombre": "PORTILLO, KENESIS EDUARDO",
        "pin": "5844",
        "m33": {'prep': 1.9, 'ejec': 4.0, 'val': 1.163, 'prelim': 7.063, 'final': 7.06, 'nivel': 4},
        "m38": {'prep': 2.19, 'ejec': 4.0, 'val': 1.95, 'prelim': 8.388, 'final': 8.39, 'nivel': 4}
    },
    "6689340": {
        "num": 20,
        "nie": "6689340",
        "nombre": "RAFAELANO CHICAS, CRISTIAN MAURICIO",
        "pin": "1557",
        "m33": {'prep': 1.9, 'ejec': 4.0, 'val': 1.163, 'prelim': 7.063, 'final': 7.06, 'nivel': 4},
        "m38": {'prep': 2.19, 'ejec': 4.0, 'val': 2.0, 'prelim': 8.438, 'final': 8.44, 'nivel': 4}
    },
    "6051310": {
        "num": 21,
        "nie": "6051310",
        "nombre": "RAMOS PASTORA, KEILY LISBETH",
        "pin": "4627",
        "m33": {'prep': 1.9, 'ejec': 4.0, 'val': 0.938, 'prelim': 7.088, 'final': 7.09, 'nivel': 4},
        "m38": {'prep': 2.5, 'ejec': 4.0, 'val': 2.1, 'prelim': 8.85, 'final': 8.85, 'nivel': 4}
    },
    "4768936": {
        "num": 22,
        "nie": "4768936",
        "nombre": "ROMERO MEDRANO, CAMILA ALEXANDRA",
        "pin": "4033",
        "m33": {'prep': 2.05, 'ejec': 5.0, 'val': 1.425, 'prelim': 8.225, 'final': 8.23, 'nivel': 4},
        "m38": {'prep': 2.44, 'ejec': 5.0, 'val': 2.3, 'prelim': 9.738, 'final': 9.74, 'nivel': 5}
    },
    "6051311": {
        "num": 23,
        "nie": "6051311",
        "nombre": "SOSA FLORES, JANETH ALERY",
        "pin": "4658",
        "m33": {'prep': 2.25, 'ejec': 5.0, 'val': 1.125, 'prelim': 8.125, 'final': 8.13, 'nivel': 4},
        "m38": {'prep': 2.5, 'ejec': 4.0, 'val': 2.3, 'prelim': 8.8, 'final': 8.8, 'nivel': 4}
    },
    "3562170": {
        "num": 24,
        "nie": "3562170",
        "nombre": "VASQUEZ PACHECO, KAREN MARISOL",
        "pin": "7287",
        "m33": {'prep': 2.3, 'ejec': 5.0, 'val': 1.425, 'prelim': 8.725, 'final': 8.73, 'nivel': 4},
        "m38": {'prep': 2.25, 'ejec': 5.0, 'val': 2.3, 'prelim': 9.3, 'final': 9.3, 'nivel': 5}
    },
    "4301220": {
        "num": 25,
        "nie": "4301220",
        "nombre": "ZELAYA SALGADO, LEYLI MARITZA",
        "pin": "3837",
        "m33": {'prep': 2.1, 'ejec': 5.0, 'val': 1.406, 'prelim': 8.256, 'final': 8.26, 'nivel': 4},
        "m38": {'prep': 2.5, 'ejec': 4.0, 'val': 2.3, 'prelim': 9.05, 'final': 9.05, 'nivel': 5}
    },
}

# Estilos CSS personalizados
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        color: #1E3A8A;
        font-weight: bold;
        margin-bottom: 0px;
    }
    .sub-header {
        text-align: center;
        color: #4B5563;
        font-size: 1.05rem;
        margin-bottom: 20px;
    }
    .card {
        background-color: #F3F4F6;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 15px;
        border-left: 5px solid #1E3A8A;
    }
    .stButton>button {
        width: 100%;
        background-color: #1E3A8A;
        color: white;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Encabezado Principal
st.markdown("<h2 class='main-header'>INSTITUTO NACIONAL DE CIUDAD BARRIOS</h2>", unsafe_allow_html=True)
st.markdown("<p class='sub-header'><b>Bachillerato Técnico Vocacional Administrativo Contable</b><br>Tercer Año - Sección 'D' (3TD 2026)<br>Profesor Encargado: José de la Paz Gutiérrez</p>", unsafe_allow_html=True)

st.divider()

# Estado de la sesión
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False
if 'alumno' not in st.session_state:
    st.session_state.alumno = None

if not st.session_state.autenticado:
    st.subheader("🔑 Acceso Privado de Estudiantes")
    st.info("Ingresa tu número de NIE y tu PIN de 4 dígitos asignado para consultar tu boleta de calificaciones.")
    
    with st.form("login_form"):
        nie_input = st.text_input("Número de NIE:", placeholder="Ej. 6051092").strip()
        pin_input = st.text_input("PIN de Acceso (4 dígitos):", type="password", placeholder="****").strip()
        submit_button = st.form_submit_button("Ingresar al Portal")
        
    if submit_button:
        if nie_input in ESTUDIANTES and ESTUDIANTES[nie_input]["pin"] == pin_input:
            st.session_state.autenticado = True
            st.session_state.alumno = ESTUDIANTES[nie_input]
            st.rerun()
        else:
            st.error("❌ El NIE o el PIN ingresado no son correctos. Por favor verifica tus credenciales.")
else:
    alumno = st.session_state.alumno
    
    st.success(f"👋 ¡Bienvenido/a, **{alumno['nombre']}**!")
    st.markdown(f"**NIE:** `{alumno['nie']}` | **Nº de Lista:** {alumno['num']}")
    
    st.markdown("### 📊 Tus Calificaciones por Módulo")
    
    # Pestañas para cada módulo
    tab1, tab2 = st.tabs(["📘 Módulo 3.3: Admón. Recurso Humano", "🚀 Módulo 3.8: Proyecto Emprendedor"])
    
    with tab1:
        m33 = alumno["m33"]
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="Nota Final del Módulo 3.3", value=f"{m33['final']:.2f} / 10")
        with col2:
            st.metric(label="Nivel de Competencia", value=f"Nivel {m33['nivel']}")
            
        st.markdown("#### Desglose de Evaluación Módulo 3.3")
        df_m33 = pd.DataFrame({
            "Criterio de Evaluación": ["Preparación (25%)", "Ejecución (50%)", "Valoración (25%)", "Nota Preliminar", "Nota Final"],
            "Puntaje Obtenido": [f"{m33['prep']:.2f}", f"{m33['ejec']:.2f}", f"{m33['val']:.3f}", f"{m33['prelim']:.3f}", f"{m33['final']:.2f}"]
        })
        st.table(df_m33)
        
    with tab2:
        m38 = alumno["m38"]
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="Nota Final del Módulo 3.8", value=f"{m38['final']:.2f} / 10")
        with col2:
            st.metric(label="Nivel de Competencia", value=f"Nivel {m38['nivel']}")
            
        st.markdown("#### Desglose de Evaluación Módulo 3.8")
        df_m38 = pd.DataFrame({
            "Criterio de Evaluación": ["Preparación (25%)", "Ejecución (50%)", "Valoración (25%)", "Nota Preliminar", "Nota Final"],
            "Puntaje Obtenido": [f"{m38['prep']:.2f}", f"{m38['ejec']:.2f}", f"{m38['val']:.3f}", f"{m38['prelim']:.3f}", f"{m38['final']:.2f}"]
        })
        st.table(df_m38)
        
    with st.expander("ℹ️ ¿Qué significan los Niveles de Competencia?"):
        st.markdown("""
        * **Nivel 5 (Excelente / 9.0 - 10.0):** Demuestra dominio completo e innovador de las competencias del módulo.
        * **Nivel 4 (Muy Bueno / 7.0 - 8.9):** Alcanza con solidez las competencias requeridas.
        * **Nivel 3 (Bueno / 6.0 - 6.9):** Cumple con el estándar mínimo aceptable.
        * **Nivel 1 - 2 (En Proceso / < 6.0):** Requiere refuerzo académico complementario.
        """)
        
    st.divider()
    if st.button("🔒 Cerrar Sesión"):
        st.session_state.autenticado = False
        st.session_state.alumno = None
        st.rerun()

st.caption("© 2026 Instituto Nacional de Ciudad Barrios - Sistema de Consulta de Notas")
