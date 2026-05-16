# APP.PY COMPLETO
# =========================================================
# Gestor de Inspecciones
# - Configuración inicial de ruta del Excel (solo primera vez)
# - Lectura de archivo .xlsm/.xlsx
# - Carga de todas las hojas que empiecen por "BD"
# - Dashboard visual moderno
# =========================================================

import os
import pandas as pd
import streamlit as st

# =========================================================
# CONFIGURACIÓN GENERAL
# =========================================================

st.set_page_config(
    page_title="Gestor de Inspecciones",
    layout="wide",
    initial_sidebar_state="expanded"
)

CONFIG_FILE = "config_ruta_excel.txt"

# =========================================================
# CSS PERSONALIZADO
# =========================================================

st.markdown("""
<style>
.main {
    background-color: #f5f7fb;
}

.block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0b1320 0%, #0f2747 100%);
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

.titulo-principal {
    font-size: 38px;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 0;
}

.subtitulo {
    color: #64748b;
    margin-top: 0;
    margin-bottom: 25px;
}

.card {
    background-color: white;
    border-radius: 16px;
    padding: 20px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.kpi {
    text-align: center;
    padding: 15px;
    border-radius: 14px;
    background: white;
    box-shadow: 0 2px 10px rgba(0,0,0,0.08);
}

.kpi h2 {
    margin: 0;
    color: #0f172a;
}

.kpi p {
    margin: 0;
    color: #64748b;
}

.badge {
    display: inline-block;
    background-color: #dbeafe;
    color: #1d4ed8;
    padding: 4px 10px;
    border-radius: 999px;
    font-weight: 600;
    font-size: 12px;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# FUNCIONES DE CONFIGURACIÓN
# =========================================================

def guardar_ruta_excel(ruta):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        f.write(ruta.strip())

def cargar_ruta_excel_guardada():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return f.read().strip()
    return ""

def obtener_ruta_excel():
    ruta_guardada = cargar_ruta_excel_guardada()

    if ruta_guardada and os.path.exists(ruta_guardada):
        return ruta_guardada

    st.title("⚙️ Configuración inicial")
    st.info(
        "Introduzca la ruta completa del archivo Excel (.xlsm o .xlsx).\n\n"
        "Esta configuración solo se solicitará la primera vez."
    )

    ruta_sugerida = (
        r"C:\Users\alejandro.lopez\OneDrive - Eurocontrol S.A"
        r"\Attachments\Documentos\IA BASES DE DATOS"
        r"\EXCEL 3.4.26.xlsm"
    )

    ruta = st.text_input(
        "Ruta completa del archivo Excel",
        value=ruta_guardada or ruta_sugerida
    )

    if st.button("✅ Guardar configuración", use_container_width=True):
        if not ruta.strip():
            st.error("Debe indicar una ruta.")
            st.stop()

        if not os.path.exists(ruta):
            st.error("El archivo no existe en la ruta indicada.")
            st.stop()

        guardar_ruta_excel(ruta)
        st.success("Ruta guardada correctamente.")
        st.rerun()

    st.stop()

RUTA_EXCEL = obtener_ruta_excel()

# =========================================================
# CARGA DE DATOS
# =========================================================

@st.cache_data(show_spinner="Cargando datos desde Excel...")
def cargar_datos():
    libro = pd.ExcelFile(RUTA_EXCEL, engine="openpyxl")

    hojas_bd = [
        hoja for hoja in libro.sheet_names
        if hoja.upper().startswith("BD")
    ]

    if not hojas_bd:
        raise ValueError(
            "No se encontraron hojas cuyo nombre comience por 'BD'."
        )

    dataframes = []

    for hoja in hojas_bd:
        df_hoja = pd.read_excel(
            RUTA_EXCEL,
            sheet_name=hoja,
            engine="openpyxl"
        )

        df_hoja = df_hoja.dropna(how="all")

        if df_hoja.empty:
            continue

        df_hoja["__HOJA_ORIGEN"] = hoja
        dataframes.append(df_hoja)

    if not dataframes:
        raise ValueError("No se encontraron datos válidos.")

    df_total = pd.concat(
        dataframes,
        ignore_index=True,
        sort=False
    )

    df_total = df_total.dropna(axis=1, how="all")
    df_total.columns = [str(c).strip() for c in df_total.columns]

    return df_total

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:
    st.markdown("# 🛠️ Gestor")
    st.markdown("### Inspecciones")

    st.divider()

    if st.button("🔄 Actualizar datos", use_container_width=True):
        st.cache_data.clear()
        st.rerun()

    st.divider()

    st.button("📋 Inspecciones", use_container_width=True)
    st.button("🛒 Carrito de trabajo", use_container_width=True)
    st.button("📁 Carpetas", use_container_width=True)
    st.button("💰 Facturar", use_container_width=True)
    st.button("🏢 Clientes", use_container_width=True)

# =========================================================
# LECTURA DEL EXCEL
# =========================================================

try:
    df = cargar_datos()
except Exception as e:
    st.error(f"Error al cargar el Excel: {e}")
    st.stop()

# =========================================================
# CABECERA
# =========================================================

st.markdown(
    '<p class="titulo-principal">📋 Gestor de Inspecciones</p>',
    unsafe_allow_html=True
)

st.markdown(
    f'<p class="subtitulo">Archivo: {os.path.basename(RUTA_EXCEL)}</p>',
    unsafe_allow_html=True
)

# =========================================================
# KPIs
# =========================================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        f'<div class="kpi"><h2>{len(df):,}</h2><p>Registros</p></div>',
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        f'<div class="kpi"><h2>{df["__HOJA_ORIGEN"].nunique()}</h2><p>Hojas BD</p></div>',
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        f'<div class="kpi"><h2>{len(df.columns)}</h2><p>Columnas</p></div>',
        unsafe_allow_html=True
    )

with c4:
    st.markdown(
        f'<div class="kpi"><h2>{os.path.basename(RUTA_EXCEL)}</h2><p>Archivo</p></div>',
        unsafe_allow_html=True
    )

st.write("")

# =========================================================
# FILTROS
# =========================================================

st.markdown('<div class="card">', unsafe_allow_html=True)

col1, col2 = st.columns([1, 3])

with col1:
    hojas = ["Todas"] + sorted(
        df["__HOJA_ORIGEN"].dropna().unique().tolist()
    )
    hoja_seleccionada = st.selectbox("Hoja", hojas)

with col2:
    busqueda = st.text_input(
        "Filtro rápido",
        placeholder="Buscar en cualquier columna..."
    )

st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# FILTRADO
# =========================================================

df_filtrado = df.copy()

if hoja_seleccionada != "Todas":
    df_filtrado = df_filtrado[
        df_filtrado["__HOJA_ORIGEN"] == hoja_seleccionada
    ]

if busqueda:
    mask = df_filtrado.astype(str).apply(
        lambda fila: fila.str.contains(
            busqueda,
            case=False,
            na=False
        ).any(),
        axis=1
    )
    df_filtrado = df_filtrado[mask]

# =========================================================
# CONTENIDO PRINCIPAL
# =========================================================

izq, der = st.columns([3, 1])

with izq:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📑 Registros")

    st.dataframe(
        df_filtrado,
        use_container_width=True,
        height=650
    )

    st.markdown('</div>', unsafe_allow_html=True)

with der:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📌 Detalle")

    if len(df_filtrado) > 0:
        fila = df_filtrado.iloc[0]

        st.markdown(f"### {fila['__HOJA_ORIGEN']}")
        st.markdown(
            '<span class="badge">Primer registro filtrado</span>',
            unsafe_allow_html=True
        )

        st.write("")

        columnas_mostrar = [
            col for col in df_filtrado.columns[:15]
            if pd.notna(fila[col]) and str(fila[col]).strip() != ""
        ]

        for col in columnas_mostrar:
            st.markdown(f"**{col}:** {fila[col]}")

        st.write("")

        st.button("🛒 Añadir al carrito", use_container_width=True)
        st.button("📄 Generar Word", use_container_width=True)
        st.button("📑 Generar PDF", use_container_width=True)
        st.button("⚙️ Procesar", use_container_width=True)
    else:
        st.info("No hay registros para mostrar.")

    st.markdown('</div>', unsafe_allow_html=True)
