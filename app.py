import streamlit as st
import pandas as pd

# =========================================================
# CONFIGURACIÓN GENERAL
# =========================================================

st.set_page_config(
    page_title="Gestor de Inspecciones",
    layout="wide",
    initial_sidebar_state="expanded"
)

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

.estado-act {
    background-color: #dcfce7;
    color: #166534;
    padding: 4px 10px;
    border-radius: 999px;
    font-weight: 600;
    font-size: 12px;
}

.estado-fac {
    background-color: #ede9fe;
    color: #6d28d9;
    padding: 4px 10px;
    border-radius: 999px;
    font-weight: 600;
    font-size: 12px;
}

.estado-bt {
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
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("# 🛠️ Gestor")
    st.markdown("### Inspecciones")

    st.divider()

    st.markdown("## Gestión")

    st.button("📋 Inspecciones", use_container_width=True)
    st.button("🛒 Carrito de trabajo", use_container_width=True)
    st.button("📁 Carpetas", use_container_width=True)
    st.button("💰 Facturar", use_container_width=True)
    st.button("🏢 Clientes", use_container_width=True)

    st.divider()

    st.markdown("## Procesos")

    st.button("⚙️ Procesar", use_container_width=True)
    st.button("✏️ Modificar", use_container_width=True)
    st.button("📌 Gestión ACT", use_container_width=True)

    st.divider()

    st.markdown("## Reportes")

    st.button("📄 Informes", use_container_width=True)
    st.button("📊 Estadísticas", use_container_width=True)

# =========================================================
# DATOS DE EJEMPLO
# =========================================================

datos = {
    "Estado": [
        "ACT", "ACT", "FAC", "BT", "BT",
        "ACT", "FAC", "BT", "ACT", "BT"
    ],

    "Código": [
        "26-64-ASC-IP-0035",
        "26-64-ASC-IP-0036",
        "26-64-ASC-IP-0169",
        "26-64-RBT-IP-0026",
        "26-64-RBT-IP-0030",
        "26-64-ASC-IP-0240",
        "26-64-ASC-IP-0273",
        "26-64-RBT-IP-0041",
        "26-64-ASC-IP-0348",
        "26-64-RBT-IP-0043"
    ],

    "Campo": [
        "ASC", "ASC", "ASC", "BT", "BT",
        "ASC", "ASC", "BT", "ASC", "BT"
    ],

    "Dirección": [
        "CALLE OLIVAR 19",
        "EDIF. DE FÁBRICA",
        "CL. SANTA MARTA, 8",
        "Sistema de Fabricación",
        "QUESERIA EL TAJO",
        "CL. CAMINO CASTILLEJOS, 5",
        "CL. HEROE DE SOSTOA, 85",
        "DIA RETAIL ESPAÑA",
        "AV GRAN BRETAÑA 1",
        "CONSUL SOCIEDAD COOP"
    ],

    "Cliente": [
        "Cliente A",
        "Cliente B",
        "INDUSTRIAS TZBSAT",
        "SAFI",
        "QUESERIA",
        "Cliente C",
        "Cliente D",
        "DIA",
        "Cliente E",
        "CONSUL"
    ],

    "Fecha": [
        "26/01/2026",
        "26/01/2026",
        "26/01/2026",
        "26/01/2026",
        "26/01/2026",
        "27/01/2026",
        "28/01/2026",
        "28/01/2026",
        "29/01/2026",
        "30/01/2026"
    ]
}

df = pd.DataFrame(datos)

# =========================================================
# CABECERA
# =========================================================

st.markdown(
    '<p class="titulo-principal">📋 Gestor de Inspecciones</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitulo">Panel de gestión moderno conectado a Excel Online</p>',
    unsafe_allow_html=True
)

# =========================================================
# KPIs
# =========================================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class="kpi">
        <h2>{len(df)}</h2>
        <p>Registros</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="kpi">
        <h2>{len(df[df['Estado']=='ACT'])}</h2>
        <p>ACT</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="kpi">
        <h2>{len(df[df['Estado']=='FAC'])}</h2>
        <p>FAC</p>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="kpi">
        <h2>{len(df[df['Estado']=='BT'])}</h2>
        <p>BT</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# =========================================================
# FILTROS
# =========================================================

with st.container():

    st.markdown('<div class="card">', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns([1,1,1,2])

    with col1:
        filtro_estado = st.selectbox(
            "Estado",
            ["Todos"] + sorted(df["Estado"].unique().tolist())
        )

    with col2:
        filtro_campo = st.selectbox(
            "Campo",
            ["Todos"] + sorted(df["Campo"].unique().tolist())
        )

    with col3:
        filtro_fecha = st.date_input("Fecha")

    with col4:
        busqueda = st.text_input(
            "Filtro rápido",
            placeholder="Buscar código, cliente, dirección..."
        )

    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# FILTRADO
# =========================================================

df_filtrado = df.copy()

if filtro_estado != "Todos":
    df_filtrado = df_filtrado[df_filtrado["Estado"] == filtro_estado]

if filtro_campo != "Todos":
    df_filtrado = df_filtrado[df_filtrado["Campo"] == filtro_campo]

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

izq, der = st.columns([3,1])

# =========================================================
# TABLA
# =========================================================

with izq:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📑 Inspecciones")

    st.dataframe(
        df_filtrado,
        use_container_width=True,
        height=600
    )

    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# PANEL DERECHO
# =========================================================

with der:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📌 Detalle")

    if len(df_filtrado) > 0:

        fila = df_filtrado.iloc[0]

        estado = fila["Estado"]

        if estado == "ACT":
            badge = '<span class="estado-act">ACT</span>'
        elif estado == "FAC":
            badge = '<span class="estado-fac">FAC</span>'
        else:
            badge = '<span class="estado-bt">BT</span>'

        st.markdown(
            f"## {fila['Código']} {badge}",
            unsafe_allow_html=True
        )

        st.write("")

        st.markdown(f"**Campo:** {fila['Campo']}")
        st.markdown(f"**Dirección:** {fila['Dirección']}")
        st.markdown(f"**Cliente:** {fila['Cliente']}")
        st.markdown(f"**Fecha:** {fila['Fecha']}")

        st.write("")

        st.button(
            "🛒 Añadir al carrito",
            use_container_width=True
        )

        st.button(
            "📄 Generar informe",
            use_container_width=True
        )

        st.button(
            "💰 Facturar",
            use_container_width=True
        )

        st.button(
            "⚙️ Procesar",
            use_container_width=True
        )

    st.markdown('</div>', unsafe_allow_html=True)
